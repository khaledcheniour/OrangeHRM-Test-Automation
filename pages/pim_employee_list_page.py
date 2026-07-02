from __future__ import annotations

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class EmployeeListPage(BasePage):
    
    PATH = "pim/viewEmployeeList"
    Employee_id="input.oxd-input.oxd-input--active"
    _search_button = 'button[type="submit"]'
    _emp_list='text="Employee List"'
    _Records_Found="span.oxd-text.oxd-text--span"
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def search_employee_id(self, employee_id: str) -> None:
        """Search for an employee by their ID."""   
        self.page.locator("input.oxd-input.oxd-input--active").fill(employee_id)
        self.page.click(self._search_button)

    def open_list(self):
        self.page.click(self._emp_list)

    def get_records_found(self):
        """Get the text of the 'Records Found' element."""
        return self.page.locator(self._Records_Found).inner_text()

    

    

    