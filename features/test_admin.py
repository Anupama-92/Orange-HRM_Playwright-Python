import re

import requests

from config.config import Configs
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from utils.employment_status_api_utils import EmploymentStatusAPI


def test_employment_status(page):
    new_status = EmploymentStatusAPI.add_employment_status()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.enter_username()
    login_page.enter_password()
    login_page.click_login()
    admin_page = AdminPage(page)
    admin_page.navigate_to_admin_page()
    admin_page.select_job_details()
    # Fetch all statuses
    ui_statuses = admin_page.get_all_employment_status()

    # Compare API response with UI list
    assert new_status in ui_statuses, f"API status '{new_status}' not found in UI statuses {ui_statuses}"

    # Save into config.py
    config_path = "config/config.py"
    with open(config_path, "r") as file:
        content = file.read()

    new_content = re.sub(
        r"EMPLOYMENT_STATUS_LIST\s*=\s*\[.*?\]",
        f"EMPLOYMENT_STATUS_LIST = {ui_statuses}",
        content,
        flags=re.DOTALL
    )

    with open(config_path, "w") as file:
        file.write(new_content)



