import pytest

from pages.login_page import LoginPage

@pytest.mark.smoke
#Test appearence of the title
@pytest.mark.login
def test_appearence_of_title(page):
    
    # Arrange / Act
    login_page = LoginPage(page)
    login_page.load()

    # Assert: the title of login page should be visible and should be "Login"
    assert login_page.is_loaded()== True, "Expected to appear the title of login page"
    assert login_page.login_title == "Login", "Expected to appear the title of login page"