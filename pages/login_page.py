"""Login page of OrangeHRM (``/auth/login``)  --  FULLY IMPLEMENTED EXAMPLE.

This page object models the login screen and the two outcomes of a login
attempt: success (you land on the Dashboard) and failure (an "Invalid
credentials" banner, or "Required" messages under empty fields).

Study it together with ``tests/test_login.py`` -- it is the template you will
follow when you implement the Week-3 features.
"""

from __future__ import annotations

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Drives a login attempt and exposes the resulting page state."""
 
    PATH = "/auth/login"

    # --- Locators (kept together at the top so they are easy to maintain) ---
    _USERNAME_INPUT = 'input[name="username"]'
    _PASSWORD_INPUT = 'input[name="password"]'
    _LOGIN_BUTTON = 'button[type="submit"]'
    _LOGIN_TITLE = ".orangehrm-login-title"

    # Shown on a FAILED login with wrong credentials.
    _ERROR_ALERT = ".oxd-alert-content-text"
    # Shown under each empty required field on an empty submit.
    _FIELD_ERROR = ".oxd-input-field-error-message"
    _DASHBOARD_HEADING ="h1:has-text('Dashboard')"
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    # --- Actions ----------------------------------------------------------

    def login(self, username: str, password: str) -> None:
        """Open the login page and submit the credentials."""
        self.load()
        # Use fill() even for empty strings so the "required" path is testable.
        self.fill(self._USERNAME_INPUT, username)
        self.fill(self._PASSWORD_INPUT, password)
        self.click(self._LOGIN_BUTTON)

    # --- State / queries (used by the tests for assertions) ---------------

    def is_loaded(self) -> bool:
        """True when the login form's title is visible."""
        return self.wait_until_visible(self._LOGIN_TITLE)
    
    #function to return the title of the login form
    @property
    def login_title(self) -> str:
        """Return the visible login form title text."""
        return self.text_of(self._LOGIN_TITLE)
    

    def login_succeeded(self) -> bool:
        """True if we navigated to the Dashboard after logging in.

        A successful OrangeHRM login redirects to ``/dashboard/index``, so we
        simply wait for that URL.
        """
        try:
            self.page.wait_for_url("**/dashboard/index")
            return True
        except Exception:
            return False

    @property
    def error_message(self) -> str:
        """The text of the 'Invalid credentials' banner after a failed login."""
        return self.text_of(self._ERROR_ALERT)

    def has_error(self) -> bool:
        """True if the invalid-credentials banner is displayed (waits for it)."""
        return self.wait_until_visible(self._ERROR_ALERT)

    def required_field_error_count(self) -> int:
        """How many 'Required' field errors are shown (after an empty submit)."""
        self.wait_until_visible(self._FIELD_ERROR)
        return self.page.locator(self._FIELD_ERROR).count()
    
    #I added this function to return the locator of the required field errors
    @property
    def required_field_errors(self) -> Locator:
        return self.page.locator(self._FIELD_ERROR)
