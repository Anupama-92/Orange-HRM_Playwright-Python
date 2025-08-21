from playwright.sync_api import Page


class UserManagementPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_management_menu = page.locator("i.oxd-icon.bi-chevron-down").nth(0)
        self.users = page.get_by_role("menuitem", name="Users")
        self.add_user = page.get_by_role("button", name="Add")
        self.user_role_dropdown = self.page.locator("//label[text()='User Role']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
        self.user_role = page.get_by_role("option", name="Admin")

    def navigate_to_user_management_page(self):
        self.page.pause()
        self.user_management_menu.click()

    def select_user_menu(self):
        self.users.click()

    def click_add_user(self):
        self.add_user.click()

    def click_user_role_dropdown(self):
        self.user_role_dropdown.first.click()

    def select_user_role(self):
        self.user_role.click()