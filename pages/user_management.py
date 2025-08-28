from playwright.sync_api import Page


class UserManagementPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_management_menu = page.locator("i.oxd-icon.bi-chevron-down").nth(0)
        self.users = page.get_by_role("menuitem", name="Users")
        self.add_user = page.get_by_role("button", name="Add")
        self.user_role_dropdown = self.page.locator("//label[text()='User Role']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
        self.status_dropdown_locator = self.page.locator("//label[text()='Status']/../following-sibling::div//div[contains(@class,'oxd-select-text-input')]")
        self.user_role = page.get_by_role("option", name="Admin")
        self.status_option = page.get_by_role("option", name="Enabled")
        self.employee_name = page.get_by_role("textbox", name="Type for hints...")
        self.username = page.locator("//label[text()='Username']/../following-sibling::div//input")
        self.password = page.locator("//label[text()='Password']/../following-sibling::div//input")
        self.confirm_password = page.locator("//label[text()='Confirm Password']/../following-sibling::div//input")
        self.save_button = page.get_by_role("button", name="Save")

    def navigate_to_user_management_page(self):
        # self.page.pause()
        self.user_management_menu.click()

    def select_user_menu(self):
        self.users.click()

    def click_add_user(self):
        self.add_user.click()

    def click_user_role_dropdown(self):
        self.user_role_dropdown.first.click()

    def select_user_role(self):
        self.user_role.click()

    def select_status(self):
        self.status_dropdown_locator.click()
        self.status_option.click()

    def enter_employee_name(self, employee_name):
        # Fill the text box
        self.employee_name.fill(employee_name)

        # Wait for the suggestion list to appear and select the matching option
        suggestion = self.page.locator(f"//div[@role='listbox']//span[text()='{employee_name}']")
        suggestion.wait_for(state="visible", timeout=5000)
        suggestion.click()

    def enter_username(self, username):
        self.username.fill(username)

    def enter_password(self, password):
        self.password.fill(password)

    def enter_confirm_password(self, confirm_password):
        self.confirm_password.fill(confirm_password)

    def click_save_button(self):
        self.save_button.click()


