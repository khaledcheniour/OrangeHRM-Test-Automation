"""Tests for the login feature  --  FULLY IMPLEMENTED EXAMPLE.

Study these tests carefully: they show the patterns you are expected to follow
when you implement the Week-3 features (add employee, admin search, add candidate).

Notice:
    * Each test has a clear Arrange / Act / Assert structure.
    * Tests use page objects (LoginPage) -- never raw selectors.
    * Valid-login uses the ``standard_user`` fixture (the OrangeHRM demo
      ``Admin`` / ``admin123`` account, which always exists).
"""

import pytest

from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.login
def test_login_with_valid_credentials(page, standard_user):
    """A user can log in with valid credentials and reach the Dashboard."""
    # Arrange / Act
    login_page = LoginPage(page)
    login_page.login(standard_user["username"], standard_user["password"])

    # Assert: landing on the Dashboard proves we are authenticated.
    assert login_page.login_succeeded(), "Expected to reach the Dashboard."


@pytest.mark.login
def test_login_with_invalid_credentials(page):
    """Logging in with a wrong password shows the 'Invalid credentials' banner."""
    # Arrange / Act
    login_page = LoginPage(page)
    login_page.login("Admin", "wrong_password")

    # Assert
    assert login_page.has_error(), "Expected an error banner for bad credentials."
    assert login_page.error_message == "Invalid credentials"


@pytest.mark.login
def test_login_with_empty_credentials(page):
    """Submitting empty fields shows a 'Required' message under each one."""
    # Arrange / Act
    login_page = LoginPage(page)
    login_page.login("", "")

    # Assert: both the username and password fields report "Required".
    assert login_page.required_field_error_count() == 2
