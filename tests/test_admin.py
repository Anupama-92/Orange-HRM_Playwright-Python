import re
import allure
import pytest

from config.config import Configs
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from utils.employment_status_api_utils import EmploymentStatusAPI


@allure.title("Validate Employment Status from API and UI")
@allure.feature("Employment Status")
@allure.story("Employment Status")
@allure.description("This test validates that employment statuses added via API are reflected correctly in the Admin UI.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.admin
def test_employment_status(page, request):
    with allure.step("Add new employment status via API"):
        new_status = EmploymentStatusAPI.add_employment_status()

    with allure.step("Login into OrangeHRM as Admin"):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.enter_username()
        login_page.enter_password()
        login_page.click_login()
        # Mark this test to save storage state for reuse
        setattr(request.node, "save_storage", True)

    with allure.step("Navigate to Admin -> Job -> Employment Status"):
        admin_page = AdminPage(page)
        admin_page.navigate_to_admin_page()
        admin_page.select_job_details()

    with allure.step("Fetch all statuses from UI"):
        ui_statuses = admin_page.get_all_employment_status()
        allure.attach(str(ui_statuses), "UI Employment Status List", allure.attachment_type.TEXT)

    with allure.step("Update config.py with fetched statuses"):
        config_path = "config/config.py"
        with open(config_path, "r") as file:
            content = file.read()

        ui_status_str = repr(ui_statuses)

        new_content = re.sub(
            r"(EMPLOYMENT_STATUS_LIST\s*=\s*)\[[^\]]*\]",
            f"\\1{ui_status_str}",
            content,
            flags=re.DOTALL
        )

        with open(config_path, "w") as file:
            file.write(new_content)

        allure.attach(new_content, "Updated Config.py", allure.attachment_type.TEXT)

    with allure.step("Compare API response with UI list"):
        assert new_status in ui_statuses, (
            f"API status '{new_status}' not found in UI statuses {ui_statuses}"
        )
