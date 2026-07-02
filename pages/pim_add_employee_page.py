from __future__ import annotations

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from utils.data_generator import Employee

class addemp(BasePage):
    PATH = "pim/addEmployee"
    _Page_subtitle = ".oxd-text.oxd-text--h6.orangehrm-main-title"
    _Add_emp='text="Add Employee"'
    _FirstName_input = 'input[name="firstName"]'
    _MiddleName_input = 'input[name="middleName"]'
    _LastName_input = 'input[name="lastName"]'
    _save_button = 'button[type="submit"]'
    _FIELD_ERROR = ".oxd-input-field-error-message"
    _PERSONAL_DETAILS_TITLE = 'text="Personal Details"'
    _EMPLOYEE_ID = "//label[normalize-space()='Employee Id']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def open(self):
        self.page.click(self._Add_emp)
        
    def is_loaded(self) -> bool:
        return self.wait_until_visible(self._Page_subtitle)
    
    def fill_employee_form(self, employee: Employee) -> None:
        """Fill the add employee form with the given employee data."""
        self.fill(self._FirstName_input, employee.first_name)
        self.fill(self._MiddleName_input, employee.middle_name)
        self.fill(self._LastName_input, employee.last_name)
        self.page.click(self._save_button)

    def required_field_error_count(self) -> int:
        """How many 'Required' field errors are shown (after an empty submit)."""
        self.wait_until_visible(self._FIELD_ERROR)
        return self.page.locator(self._FIELD_ERROR).count()
    def get_employee_id(self) -> str:
        """Get the employee ID from the form."""
        return self.page.locator(self._EMPLOYEE_ID).input_value()
    def personal_details_loaded(self) -> bool:
        """Check if the personal details page is loaded after submission."""
        return self.wait_until_visible(self._PERSONAL_DETAILS_TITLE)