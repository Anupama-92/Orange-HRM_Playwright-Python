import json
import pytest
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from pages.user_management import UserManagementPage


def load_test_data():
    with open("test_data/user_data.json", "r") as file:
        return json.load(file)


@pytest.mark.parametrize("user", load_test_data())
def test_user_management(page, user):
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

    # Dynamic data from JSON
    user_management_page.click_user_role_dropdown()
    user_management_page.select_user_role()  # You can also make role dynamic if needed
    user_management_page.select_status()
    user_management_page.enter_employee_name(user["employee_name"])
    user_management_page.username.fill(user["username"])
    user_management_page.password.fill(user["password"])
    user_management_page.confirm_password.fill(user["confirm_password"])
    user_management_page.click_save_button()
