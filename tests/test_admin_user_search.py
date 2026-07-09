import pytest
from pages.dashboard_page import DashboardPage
from pages.admin_user_page import adminuserPage

@pytest.mark.smoke
@pytest.mark.login
def test_search_user_by_username(dashboard: DashboardPage):
    dashboard.open_menu("Admin")

    admin_user_page = adminuserPage(dashboard.page)
    
    # Check that the Admin User page is loaded
    assert admin_user_page.is_loaded(), "Admin User page is not loaded"
    
    # Search for a user by username
    username_to_search = "admin"  
    admin_user_page.search_username(username_to_search)
    
    # Verify that the search results contain the expected username
    records_found = admin_user_page.number_of_records()
    assert records_found > 0, f"No records found for username '{username_to_search}'"