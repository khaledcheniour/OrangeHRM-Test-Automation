
from operator import contains

import pytest
import pages.login_page
@pytest.mark.smoke
@pytest.mark.login
# testing if the dashboard header is visible after login
def test_dashboard_header(dashboard):
    
    assert dashboard.is_loaded(), "Dashboard header is not visible after login"

# testing if the dashboard menu items are present and correct and if the number of menu items is correct  
def test_dashboard_menu_items(dashboard):
    menu_texts = dashboard.get_elements_text(dashboard._menu_items)
    expected_menu_items = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Claim", "Buzz"]
    i=0
    for a in expected_menu_items:
        i+=1
        assert a in menu_texts, f"Expected menu item: {a}, but got: {menu_texts}"
    assert i==len(expected_menu_items), f"Expected {len(expected_menu_items)} menu items, but got {i}"


# testing if the dashboard menu items are clickable and if the header changes accordingly

def test_menu_items_navigation(dashboard):
    expected_menu_items = ["Admin", "PIM", "Leave", "Time", "Recruitment", "Performance", "Dashboard", "Directory", "Claim", "Buzz"]
    for menu_item in expected_menu_items:
        dashboard.open_menu(menu_item)
        assert contains(dashboard.text_of(dashboard._Dashboard_Header), menu_item), f"Expected header: {menu_item}, but got: {dashboard.text_of(dashboard._Dashboard_Header)}"

#testing if navigation to the maintenance menu item requires password and if the header changes accordingly
def test_maintenance_menu_item_navigation(dashboard, standard_user):
    dashboard.open_menu("Maintenance")
    assert contains(dashboard.text_of(dashboard._administrator_access_header), "Administrator Access"), f"Expected header: Administrator Access, but got: {dashboard.text_of(dashboard._Dashboard_Header)}"

    dashboard.fill(dashboard._PASSWORD_INPUT, standard_user["password"])
    dashboard.click('button[type="submit"]')
    assert contains(dashboard.text_of(dashboard._Dashboard_Header), "Maintenance"), f"Expected header: Maintenance, but got: {dashboard.text_of(dashboard._Dashboard_Header)}"

# testing navigation to my info menu item and if the header shows PIM
def test_my_info_menu_item_navigation(dashboard):
    dashboard.open_menu("My Info")
    assert contains(dashboard.text_of(dashboard._Dashboard_Header), "PIM"), f"Expected header: PIM, but got: {dashboard.text_of(dashboard._Dashboard_Header)}"

def test_logout(dashboard):
    dashboard.logout()
    assert pages.login_page.LoginPage(dashboard.page).login_title == "Login", "Expected to appear the title of login page"