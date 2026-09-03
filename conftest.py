"""Project-wide pytest fixtures.

``conftest.py`` is automatically discovered by pytest. Anything defined here is
available to every test without an explicit import. We use it to:

    * apply our window-size / timeout settings to the browser that
      ``pytest-playwright`` creates for us, and
    * provide convenient, reusable fixtures such as the demo credentials and an
      already-logged-in dashboard.

The ``page`` fixture itself comes from the ``pytest-playwright`` plugin -- it is
a fresh browser tab, isolated per test.
"""

from __future__ import annotations

import pytest
from playwright.sync_api import Page

from config.config import settings
#from pages._page import DashboardPage
from pages.login_page import LoginPage
from utils.data_generator import Candidate, Employee, generate_candidate, generate_employee


# ---------------------------------------------------------------------------
# Apply our settings to the browser pytest-playwright launches.
# These fixtures override the ones with the same name shipped by the plugin.
# (Headed mode, slow-mo and browser choice use the native --headed / --slowmo /
#  --browser flags instead -- see the README.)
# ---------------------------------------------------------------------------
@pytest.fixture
def browser_context_args(browser_context_args: dict) -> dict:
    """Give every browser context a consistent window size."""
    return {
        **browser_context_args,
        "viewport": {"width": 1366, "height": 768},
        "ignore_https_errors": True,
    }


@pytest.fixture(autouse=True)
def _set_default_timeout(page: Page) -> None:
    """Apply our default timeout to every test's page automatically."""
    page.set_default_timeout(settings.default_timeout)


# ---------------------------------------------------------------------------
# Convenience fixtures the tests can request by name.
# ---------------------------------------------------------------------------
@pytest.fixture
def standard_user() -> dict[str, str]:
    """The OrangeHRM demo administrator credentials (from config).

    This account always exists and has full access, which makes it the reliable
    way to test the logged-in features (PIM, Admin, Recruitment, ...).
    """
    return {"username": settings.username, "password": settings.password}


@pytest.fixture
def new_employee() -> Employee:
    """Fresh random employee data (different on every run)."""
    return generate_employee()


@pytest.fixture
def new_candidate() -> Candidate:
    """Fresh random candidate data with a unique email (different every run)."""
    return generate_candidate()


@pytest.fixture
def dashboard(page: Page, standard_user: dict[str, str]) -> DashboardPage:
    """An authenticated session: logs in the demo admin and returns the Dashboard.

    Use this when your test needs to be logged in but does not care *how* -- it
    lets you jump straight to the feature under test. From the returned
    ``DashboardPage`` you can navigate via ``open_menu(...)``, or simply
    ``SomeFeaturePage(page).load()`` to go directly to a feature's URL.
    """
    LoginPage(page).login(standard_user["username"], standard_user["password"])
    dash = DashboardPage(page)
    # Make sure we are actually authenticated before the test continues.
    assert dash.is_logged_in(), "Setup failed: could not log in the demo user."
    return dash
