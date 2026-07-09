from __future__ import annotations
from operator import index

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class adminuserPage(BasePage):
    
    PATH = "admin/viewSystemUsers"
    _username = "//div[contains(@class,'oxd-input-group')][.//label[normalize-space()='Username']]//input"
    _search_button = 'button[type="submit"]'
    _system_users='text="System Users"'

    _Record_count="//span[contains(., 'Found')]"
    _next_button = "//button[contains(@class, 'oxd-pagination-page-item--previous-next')][.//i[contains(@class, 'bi-chevron-right')]]"
    def __init__(self, page: Page) -> None:
        super().__init__(page)

     
    def is_loaded(self) -> bool:
        return self.wait_until_visible(self._system_users)
    
    def number_of_records(self) -> int:
        """Extract the count of records from the 'Records Found' text."""
        records_text = self.page.locator(self._Record_count).inner_text()
        # Assuming the format is "(X) Record(s) Found", we can extract the number.
        num_records = ""
        for i in records_text:
            if i.isdigit():
                num_records +=i 
        return int(num_records)
    def search_username(self, username: str) -> None:
        """Search for a user by their username."""   
        self.page.locator(self._username).fill(username)
        self.page.click(self._search_button)