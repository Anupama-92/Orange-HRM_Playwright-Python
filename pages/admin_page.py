from playwright.sync_api import Page

from config.config import Configs


class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_menu = page.get_by_role("link", name="Admin")
        self.job_menu = page.locator("i.oxd-icon.bi-chevron-down").nth(1)
        self.employment_status = page.get_by_role("menuitem", name="Employment Status")
        self.employment_status_list = page.locator("//div[@role='row']//div[2]")

    def navigate_to_admin_page(self):
        self.admin_menu.click()

    def select_job_details(self):
        self.job_menu.click()
        self.employment_status.click()

    def get_all_employment_status(self):
        # Wait until at least one status cell is visible
        self.page.wait_for_selector("div.oxd-table-cell[role='cell'][style*='flex-basis: 80%'] div", timeout=5000)

        statuses = self.page.locator(
            "div.oxd-table-cell[role='cell'][style*='flex-basis: 80%'] div"
        ).all_text_contents()

        print("DEBUG: Employment statuses from UI:", statuses)
        return [s.strip() for s in statuses if s.strip()]
