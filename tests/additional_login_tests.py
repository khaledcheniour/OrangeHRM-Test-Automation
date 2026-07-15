import pytest

from pages.login_page import LoginPage
from playwright.sync_api import expect

@pytest.mark.smoke
@pytest.mark.login
def test_login_with_username_containing_spaces_at_end(page, standard_user):
    """A user can log in with valid credentials and reach the Dashboard."""
    # Arrange / Act
    
    login_page = LoginPage(page)
    login_page.login(standard_user["username"]+"     ", standard_user["password"])

    # Assert: landing on the Dashboard proves we are authenticated.

    assert login_page.login_succeeded(), "Expected to reach the Dashboard."
    
@pytest.mark.smoke
@pytest.mark.login
def test_login_with_spaces(page):
    """Submitting spaces in fields shows a 'Required' message under each one."""
    # Arrange / Act
    login_page = LoginPage(page)
    login_page.login("     ", "     ")

    # Assert: both the username and password fields report "Required".
    assert login_page.required_field_error_count() == 2, "Expected both fields to report 'Required'."
    

@pytest.mark.login
def test_login_with_one_empty_credential(page, standard_user):
    """Submitting one empty field shows a 'Required' message under each one."""
    # Arrange / Act
    login_page = LoginPage(page)
    login_page.login(standard_user["username"], "")

    # Assert: only password field report "Required".
    assert login_page.required_field_error_count() == 1, "Expected only the password field to report 'Required'."


