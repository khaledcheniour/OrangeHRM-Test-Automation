import pytest
from pages.dashboard_page import DashboardPage
from pages.recruitment_add_candidate_page import AddCandidatePage
from utils.data_generator import Candidate



@pytest.mark.recruitment
def test_add_candidate(dashboard: DashboardPage, new_candidate: Candidate):
    dashboard.open_menu("Recruitment")

    add_candidate_page = AddCandidatePage(dashboard.page)
    add_candidate_page.open_add_candidate_form()
    
    assert add_candidate_page.is_loaded(), "Add Candidate page is not loaded"
    
    add_candidate_page.fill_candidate_form(new_candidate)
    assert add_candidate_page.wait_until_visible(add_candidate_page._Candidate_Profile), "Candidate Profile page is not loaded after adding candidate"
   # Verify that the candidate was added successfully
    # This could be done by checking for a success message or searching for the candidate in the list
    # For example:
    # assert add_candidate_page.is_success_message_displayed(), "Candidate was not added successfully"