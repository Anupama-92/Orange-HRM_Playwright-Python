from playwright.sync_api import Page

from config.config import Configs


class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_menu = page.get_by_role("link", name="Admin")
        self.job_menu = page.locator("i.oxd-icon.bi-chevron-down").nth(1)
        self.employment_status = page.get_by_role("menuitem", name="Employment Status")
        self.employment_status_list = page.locator(".oxd-table-body .oxd-table-row")

    def navigate_to_admin_page(self):
        self.admin_menu.click()

    def select_job_details(self):
        self.job_menu.click()
        self.employment_status.click()

    def get_all_employment_status(self):
        return self.employment_status_list.all_text_contents()
