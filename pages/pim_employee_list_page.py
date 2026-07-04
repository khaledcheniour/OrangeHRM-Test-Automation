from __future__ import annotations
from operator import index

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class EmployeeListPage(BasePage):
    
    PATH = "pim/viewEmployeeList"
    Employee_id="//div[contains(@class,'oxd-input-group')][.//label[normalize-space()='Employee Id']]//input"
    _search_button = 'button[type="submit"]'
    _emp_list='text="Employee List"'
    _emp_info='text="Employee Information"'
    _Records_Found="//span[normalize-space()='(1) Record Found']"
    _Record_count="//span[contains(., 'Found')]"
    _next_button = "//button[contains(@class, 'oxd-pagination-page-item--previous-next')][.//i[contains(@class, 'bi-chevron-right')]]"
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
    
    def is_loaded(self) -> bool:
        return self.wait_until_visible(self._emp_info)

    def number_of_records(self) -> int:
        """Extract the count of records from the 'Records Found' text."""
        records_text = self.page.locator(self._Record_count).inner_text()
        # Assuming the format is "(X) Record(s) Found", we can extract the number.
        num_records = ""
        for i in records_text:
            if i.isdigit():
                num_records +=i 
        return int(num_records)
    
    def extract_employee_id(self, index: int) -> str:
        rows = self.page.locator(".oxd-table-card")
        row = rows.nth(index - 1)
        return row.locator("div").first.inner_text()
    def extract_number_of_rows(self) -> int:
        """Extract the number of rows in the employee list table."""
        rows = self.page.locator(".oxd-table-card")
        count = rows.count()
        return count
    def has_next_page(self) -> bool:
        """Check if there is a next page in the employee list."""
        next_button = self.page.locator(self._next_button)
        return next_button.is_visible()
    def go_to_next_page(self) -> None:
        """Navigate to the next page in the employee list."""
        next_button = self.page.locator(self._next_button)
        next_button.click()
        self.wait_until_visible(self._Record_count)  # Wait for the page to load after clicking next
   

