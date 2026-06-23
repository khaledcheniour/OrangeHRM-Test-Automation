import pytest

from pages.login_page import LoginPage
from playwright.sync_api import expect

@pytest.mark.login
@pytest.mark.parametrize(
    "username, password, expected_field_errors, expected_banner_error",
    [
        # Case 1: Spaces in both fields
        ("     ", "     ", 2, None),
        
        # Case 2: One empty field (Using a placeholder string since 'standard_user' fixture can't be used directly inside the parameter list)
        ("Admin", "", 1, None), 
        
        # Case 3: Invalid credentials
        ("Admin", "wrong_password", 0, "Invalid credentials"),

        # Case 4: empty credentials (both fields empty)
        ("", "", 2, None),

        # Case 5: Valid credentials 
        ("Admin", "admin123", 0, None),
        
        # Case 6: Username with trailing spaces (valid credentials)
        ("Admin   ", "admin123", 0, None)
    ]
)
def test_login_validation_cases(page, username, password, expected_field_errors, expected_banner_error):
    # Arrange / Act
    login_page = LoginPage(page)
    login_page.login(username, password)

    # Assert 1: Check the count of "Required" field errors
    assert login_page.required_field_error_count() == expected_field_errors, f"Expected {expected_field_errors} 'Required' field errors."
    # expect(login_page.required_field_errors).to_have_count(expected_field_errors)

    # Assert 2: Check the banner error if one is expected
    if expected_banner_error:
        assert login_page.has_error(), f"Expected an error banner: '{expected_banner_error}'"
        assert login_page.error_message == expected_banner_error, f"Expected an error banner: '{expected_banner_error}'"
        # expect(login_page.page.locator(login_page._ERROR_ALERT)).to_be_visible()
        # expect(login_page.page.locator(login_page._ERROR_ALERT)).to_have_text(expected_banner_error)
    else:
        assert not login_page.has_error(), "Did not expect an error banner to appear."
        # expect(login_page.page.locator(login_page._ERROR_ALERT)).not_to_be_visible()