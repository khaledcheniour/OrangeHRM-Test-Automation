import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_user_page import adminuserPage
from pages.pim_add_employee_page import addemp as AddEmployeePage
from utils.data_generator import Employee

@pytest.mark.admin
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

@pytest.mark.admin   
def test_add_new_admin(page,dashboard: DashboardPage, new_employee: Employee):
    dashboard.open_menu("PIM")

    add_employee_page = AddEmployeePage(dashboard.page)
    add_employee_page.open()
    assert add_employee_page.is_loaded(), "Add Employee page is not loaded"
    

    add_employee_page.fill_employee_form(new_employee)
    
    dashboard.open_menu("Admin")

    admin_user_page = adminuserPage(dashboard.page)
    
    # Check that the Admin User page is loaded
    assert admin_user_page.is_loaded(), "Admin User page is not loaded"
    admin_user_page.page.click(admin_user_page._Add_button)
    admin_user_page.fill_Add_User_form(new_employee)

    admin_user_page.wait_for_loading_done()
    
    username_to_search = new_employee.first_name  # Assuming the username is the first name of the employee
    admin_user_page.search_username(username_to_search)
    
    # Verify that the search results contain the expected username
    records_found = admin_user_page.number_of_records()
    assert records_found == 1, f"No records found for username '{username_to_search}'"

    dashboard.logout()

    login_page = LoginPage(page)
    login_page.login(new_employee.first_name, "Admin@123")

    assert login_page.login_succeeded(), "Expected to reach the Dashboard after logging in with new user."

