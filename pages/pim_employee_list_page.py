from __future__ import annotations

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class EmployeeListPage(BasePage):
    
    PATH = "pim/viewEmployeeList"
    Employee_id="//div[contains(@class,'oxd-input-group')][.//label[normalize-space()='Employee Id']]//input"
    _search_button = 'button[type="submit"]'
    _emp_list='text="Employee List"'
    _Records_Found="//span[normalize-space()='(1) Record Found']"
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def search_employee_id(self, employee_id: str) -> None:
        """Search for an employee by their ID."""   
        self.page.locator(self.Employee_id).fill(employee_id)
        self.page.click(self._search_button)

    def open_list(self):
        self.page.click(self._emp_list)

    def get_records_found(self):
        """Get the text of the 'Records Found' element."""
        return self.page.locator(self._Records_Found).inner_text()

    

    

    