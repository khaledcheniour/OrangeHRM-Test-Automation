"""Base class shared by every Page Object.

The Page Object Model (POM) is a design pattern where each page (or major
component) of the web app gets its own class. Those classes all inherit from
``BasePage`` so they share the same small set of helper methods and the same
reference to the Playwright ``Page``.

Key ideas for the interns:
    * A page object NEVER contains assertions about *test* outcomes. It only
      models the page (locators + actions). Assertions live in the tests.
    * Prefer Playwright's built-in auto-waiting locators over manual sleeps.
      ``page.locator(...)`` waits for elements automatically.
"""

from __future__ import annotations
from random import random

from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from config.config import settings
import random

class BasePage:
    """Parent class for all page objects.

    :param page: the Playwright ``Page`` (a single browser tab) the test drives.
    """

    # Sub-classes that map to a fixed URL set this to a relative path,
    # e.g. "/pim/addEmployee". Pages reached only by clicking around leave it None.
    PATH: str | None = None

    def __init__(self, page: Page) -> None:
        self.page = page

    # --- Navigation -------------------------------------------------------

    def load(self) -> "BasePage":
        """Navigate directly to this page using its ``PATH``.

        Returns ``self`` so calls can be chained, e.g. ``LoginPage(page).load()``.
        """
        if self.PATH is None:
            raise NotImplementedError(
                f"{type(self).__name__} has no PATH set, so it cannot be loaded "
                "directly. Reach it by navigating from another page instead."
            )
        self.page.goto(f"{settings.base_url}{self.PATH}")
        return self

    @property
    def title(self) -> str:
        """The current page <title>."""
        return self.page.title()

    @property
    def current_url(self) -> str:
        """The current browser URL."""
        return self.page.url

    # --- Tiny convenience wrappers ---------------------------------------
    # These are intentionally thin. In real tests you will often use
    # ``self.page.locator(...)`` directly together with Playwright's
    # web-first assertions (``expect(...)``).

    def click(self, selector: str) -> None:
        """Click the first element matching ``selector`` (auto-waits)."""
        self.page.locator(selector).click()

    def fill(self, selector: str, value: str) -> None:
        """Clear and type ``value`` into the element matching ``selector``."""
        self.page.locator(selector).fill(value)

    def text_of(self, selector: str) -> str:
        """Return the trimmed inner text of the element matching ``selector``."""
        return self.page.locator(selector).inner_text().strip()

    def is_visible(self, selector: str) -> bool:
        """Return True if the element matching ``selector`` is visible *right now*.

        This does NOT wait -- it answers about the current moment. Use it when
        you already know the page has settled. To wait for something to appear
        (e.g. a result after submitting a form), use :meth:`wait_until_visible`.
        """
        return self.page.locator(selector).is_visible()

    def wait_until_visible(self, selector: str, timeout: int | None = None) -> bool:
        """Wait up to ``timeout`` ms for ``selector`` to become visible.

        Returns True if it appeared in time, False otherwise. This is the safe
        way to check the *result* of an action (a success banner, an error
        message, a page that loads asynchronously) without using brittle sleeps.
        """
        try:
            self.page.locator(selector).first.wait_for(
                state="visible",
                timeout=timeout if timeout is not None else settings.default_timeout,
            )
            return True
        except PlaywrightTimeoutError:
            return False

    def wait_for_loading_done(self) -> None:
        """Wait for OrangeHRM's AJAX loading spinner to finish.

        OrangeHRM reloads tables (after a search, filter, etc.) via AJAX and
        shows a circular ``.oxd-loading-spinner`` while it works. Waiting for
        that spinner to disappear is far more reliable than a fixed sleep or
        ``networkidle``, because it tracks the *actual* UI state.
        """
        spinner = self.page.locator(".oxd-loading-spinner")
        # The spinner may flash by quickly; it's fine if we never catch it.
        try:
            spinner.first.wait_for(state="visible", timeout=2_000)
        except PlaywrightTimeoutError:
            pass
        # If a spinner is (or was) showing, wait for it to go away.
        try:
            spinner.first.wait_for(state="hidden", timeout=settings.default_timeout)
        except PlaywrightTimeoutError:
            pass

    # --- OrangeHRM-specific helpers --------------------------------------
    # OrangeHRM is built with a custom Angular component library ("oxd-*").
    # Inputs are found by their <label> text, and dropdowns are NOT native
    # <select> elements, so these two helpers wrap those patterns once here.

    def fill_by_label(self, label: str, value: str) -> None:
        """Fill the text input whose form group contains the given ``label``.

        Many OrangeHRM inputs have no stable ``name`` attribute, so we locate
        them via the visible label text instead -- a robust, readable strategy.
        """
        group = self.page.locator(
            f'.oxd-input-group:has(label:text-is("{label}"))'
        )
        group.locator("input").fill(value)

    def select_dropdown_by_label(self, label: str, option: str) -> None:
        """Pick ``option`` from the oxd dropdown whose label is ``label``.

        OrangeHRM dropdowns are custom widgets: you click the control to open
        it, then click the desired option from the list that appears.
        """
        group = self.page.locator(
            f'.oxd-input-group:has(label:text-is("{label}"))'
        )
        group.locator(".oxd-select-text").click()
        self.page.locator(
            f'.oxd-select-dropdown .oxd-select-option:has-text("{option}")'
        ).first.click()
    def get_elements_text(self, selector: str) -> list[str]:
        """Return a list of trimmed inner text from all elements matching ``selector``."""
        return [text.strip() for text in self.page.locator(selector).all_inner_texts()]

    def select_random_dropdown_option(self, label: str) -> str:
        """Pick a random option from the oxd dropdown whose label is ``label``.
        
        Returns the text of the selected option so the test can verify what was chosen.
        """
        group = self.page.locator(
            f'.oxd-input-group:has(label:text-is("{label}"))'
        )
        group.locator(".oxd-select-text").click()
        
        # Get all available options
        options = self.page.locator(
            '.oxd-select-dropdown .oxd-select-option'
        ).all()
        
        # Select a random one
        random_option = random.choice(options)
        selected_text = random_option.inner_text().strip()
        random_option.click()
        
        return selected_text