import pytest
from pages.login_page import LoginPage


def test_valid_login(page):
    login_page = LoginPage(page)

    # Navigate and perform login
    login_page.navigate()
    login_page.enter_username()
    login_page.enter_password()
    login_page.click_login()

    # Assertion - check if Dashboard is visible
    assert login_page.dashboard_header.is_visible(), "Login failed - Dashboard not visible"
