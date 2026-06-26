from __future__ import annotations

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class DashboardPage(BasePage):
    """Drives a login attempt and exposes the resulting page state."""
 
    PATH = "/dashboard/index"
    _Dashboard_Header = ".oxd-topbar-header-breadcrumb-module"
    _menu_items = ".oxd-main-menu-item--name"
    
    def __init__(self, page: Page) -> None:
        super().__init__(page)
    
    def is_logged_in(self) -> bool:
        """Check if user is logged in by verifying Dashboard is accessible."""
        return self.is_visible(self._Dashboard_Header)  #make sure the dashboard header is visible to confirm login