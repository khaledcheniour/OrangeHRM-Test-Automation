from __future__ import annotations
from operator import index

from playwright.sync_api import Locator, Page
from utils.data_generator import Candidate
from pages.base_page import BasePage


class AddCandidatePage(BasePage):
    
    PATH = "recruitment/viewCandidates"
    _recruitment='text="Recruitment"'
    _Add_Button="//button[contains(., 'Add')]"
    _Candidate_Profile='text="Candidate Profile"'
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def is_loaded(self) -> bool:
        return self.wait_until_visible(self._recruitment)
    
    def open_add_candidate_form(self) -> None:
        self.click(self._Add_Button)
    def fill_candidate_form(self, Candidate: Candidate) -> None:
        """Fill the add candidate form with the given candidate data."""
        self.fill('input[name="firstName"]', Candidate.first_name)
        self.fill('input[name="lastName"]', Candidate.last_name)
        self.fill_by_label('Email', Candidate.email)
        self.fill_by_label('Contact Number', Candidate.phone)
        # BasePage.select_dropdown_by_label(BasePage, "Vacancy", BasePage.select_random_dropdown_option(BasePage, "Vacancy"))        # Assuming there's a save button to submit the form
        self.click('button[type="submit"]')


    