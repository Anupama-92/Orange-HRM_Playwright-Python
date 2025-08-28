import json
import pytest
import allure
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from pages.user_management import UserManagementPage


def load_test_data():
    with open("test_data/user_data.json", "r") as file:
        return json.load(file)


@pytest.mark.parametrize("user", load_test_data())
@allure.feature("User Management")
@allure.story("Add User")
@allure.severity(allure.severity_level.CRITICAL)
def test_user_management(page, user):
    with allure.step("Login to the application"):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.enter_username()
        login_page.enter_password()
        login_page.click_login()

    with allure.step("Navigate to Admin Page"):
        admin_page = AdminPage(page)
        admin_page.navigate_to_admin_page()

    with allure.step("Open User Management section"):
        user_management_page = UserManagementPage(page)
        user_management_page.navigate_to_user_management_page()
        user_management_page.select_user_menu()
        user_management_page.click_add_user()

    with allure.step("Fill in user details and save"):
        user_management_page.click_user_role_dropdown()
        user_management_page.select_user_role()
        user_management_page.select_status()
        user_management_page.enter_employee_name(user["employee_name"])
        user_management_page.username.fill(user["username"])
        user_management_page.password.fill(user["password"])
        user_management_page.confirm_password.fill(user["confirm_password"])
        user_management_page.click_save_button()

    # Capture screenshot and attach to Allure report
    allure.attach(
        page.screenshot(full_page=True),
        name="User Management Screen",
        attachment_type=allure.attachment_type.PNG
    )
