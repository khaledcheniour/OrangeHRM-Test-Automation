
from operator import contains

import pytest

#from pages.dashboard_page import DashboardPage
@pytest.mark.smoke
@pytest.mark.login
def test_dashboard_header(dashboard):
    
    assert dashboard.wait_until_visible(dashboard._Dashboard_Header), "expect dashboard header to be visible"
   
   
def test_dashboard_menu_items(dashboard):
    menu_texts = dashboard.get_elements_text(dashboard._menu_items)
    expected_menu_items = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Claim", "Buzz"]
    i=0
    for a in expected_menu_items:
        i+=1
        assert a in menu_texts, f"Expected menu item: {a}, but got: {menu_texts}"
    assert i==len(expected_menu_items), f"Expected {len(expected_menu_items)} menu items, but got {i}"


x

def test_menu_items_navigation(dashboard):
    expected_menu_items = ["Admin", "PIM", "Leave", "Time", "Recruitment", "Performance", "Dashboard", "Directory", "Claim", "Buzz"]
    for menu_item in expected_menu_items:
        dashboard.click('text="{}"'.format(menu_item))
        assert contains(dashboard.text_of(dashboard._Dashboard_Header), menu_item), f"Expected header: {menu_item}, but got: {dashboard.text_of(dashboard._Dashboard_Header)}"
        