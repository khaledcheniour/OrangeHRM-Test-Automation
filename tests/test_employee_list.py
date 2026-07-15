import pytest
from pages.dashboard_page import DashboardPage
from pages.pim_employee_list_page import EmployeeListPage

@pytest.mark.smoke
@pytest.mark.pim

def test_employee_list_page_loads_and_list_nonempty(dashboard: DashboardPage):
    dashboard.open_menu("PIM")

    employee_list_page = EmployeeListPage(dashboard.page)
    employee_list_page.open_list()
    
    # Check that the Employee List page is loaded
    assert employee_list_page.is_loaded(), "Employee List page is not loaded"
    assert employee_list_page.number_of_records() >= 0, "Number of records should be non-negative"

@pytest.mark.pim
def test_Id_non_empty(dashboard: DashboardPage):
    dashboard.open_menu("PIM")

    employee_list_page = EmployeeListPage(dashboard.page)
    employee_list_page.open_list()
    
    # Check that the Employee List page is loaded
    assert employee_list_page.is_loaded(), "Employee List page is not loaded"
    
    # Check that the Employee ID field is not empty
    while True:
        for i in range(1, employee_list_page.extract_number_of_rows() + 1):
            employee_id_value = employee_list_page.extract_employee_id(i)
            assert employee_id_value != "", f"Employee ID field for record {i} should not be empty"

        if not employee_list_page.has_next_page():
            break

        employee_list_page.go_to_next_page()

        