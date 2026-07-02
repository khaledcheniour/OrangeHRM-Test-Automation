
import pytest
from pages.dashboard_page import DashboardPage
from pages.pim_add_employee_page import addemp as AddEmployeePage
from utils.data_generator import Employee
from pages.pim_employee_list_page import EmployeeListPage

@pytest.mark.smoke
@pytest.mark.login
def test_add_employee_same_id(dashboard: DashboardPage, new_employee: Employee):
    dashboard.open_menu("PIM")

    add_employee_page = AddEmployeePage(dashboard.page)
    add_employee_page.open()
    assert add_employee_page.is_loaded(), "Add Employee page is not loaded"
    

    add_employee_page.fill_employee_form(new_employee)
    a=add_employee_page.get_employee_id()
    

    assert add_employee_page.personal_details_loaded(), "Personal Details page is not loaded after submission"

    Employee_list_page = EmployeeListPage(dashboard.page)
    Employee_list_page.open_list()
    Employee_list_page.search_employee_id(a)
    assert Employee_list_page.get_records_found() == "(1) Record Found", "Employee not found in the list after adding"

def test_add_employee_required_fields(dashboard: DashboardPage):
    dashboard.open_menu("PIM")

    add_employee_page = AddEmployeePage(dashboard.page)
    add_employee_page.open()
    
    assert add_employee_page.is_loaded(), "Add Employee page is  loaded"

    # Submit the form without filling any fields.
    add_employee_page.page.click(add_employee_page._save_button)

    # Check that the required field errors are shown.
    
    assert add_employee_page.required_field_error_count() ==2, "No required field errors were shown after empty submission"
   
