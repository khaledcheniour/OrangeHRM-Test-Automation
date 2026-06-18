import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #Login with valid credentials
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("admin")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    #logout
    page.locator(".oxd-userdropdown-name").click()
    page.get_by_role("menuitem", name="Logout").click()

    #Login with invalid credentials
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("amin                     ")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    #check if the login is successful when adding spaces at the end of the  username 
    page.get_by_placeholder("Username").fill("admin                        ")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    #Acces the PIM page and add a new employee
    page.get_by_role("link", name="PIM").click()
    
    page.get_by_role("button", name=" Add").click()
    page.get_by_placeholder("First Name").click()
    page.get_by_placeholder("First Name").fill("karim")
    page.get_by_placeholder("Middle Name").click()
    page.get_by_placeholder("Middle Name").fill("abdul")
    page.get_by_placeholder("Last Name").click()
    page.get_by_placeholder("Last Name").fill("hafidh")
    page.locator("form").get_by_role("textbox").nth(4).click()
    page.locator("form").get_by_role("textbox").nth(4).fill("0491555")
    page.get_by_role("button", name="Save").click()
    #logout
    
    page.locator(".oxd-userdropdown-name").click()
    page.get_by_role("menuitem", name="Logout").click()
