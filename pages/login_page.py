
from playwright.sync_api import Page
from config.config import Configs


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(Configs.BASE_URL)


