from playwright.sync_api import Page

from config.config import Configs
from behave import given, when, then


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.dashboard_header = page.get_by_role("heading", name="Dashboard")

    def navigate(self):
        self.page.goto(Configs.BASE_URL)

    def enter_username(self):
        self.username_input.fill(Configs.USERNAME)

    def enter_password(self):
        self.password_input.fill(Configs.PASSWORD)

    def click_login(self):
        self.login_button.click()
        self.dashboard_header.is_visible()

