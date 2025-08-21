from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from pages.user_management import UserManagementPage


def test_user_management(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.enter_username()
    login_page.enter_password()
    login_page.click_login()
    admin_page = AdminPage(page)
    admin_page.navigate_to_admin_page()
    user_management_page = UserManagementPage(page)
    user_management_page.navigate_to_user_management_page()
    user_management_page.select_user_menu()
    user_management_page.click_add_user()
    user_management_page.click_user_role_dropdown()
    user_management_page.select_user_role()

