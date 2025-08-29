import pytest
import allure
import os
from pages.login_page import LoginPage


@allure.title("Valid Login Test")
@allure.description("This test validates that a valid user can log into OrangeHRM successfully.")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.login
def test_valid_login(page, request):
    login_page = LoginPage(page)

    log_file = os.path.join(os.getcwd(), f"network_logs_{request.node.name}.txt")

    with open(log_file, "w", encoding="utf-8") as f:

        def log_request(req):
            f.write(f" Request: {req.method} {req.url}\n")

        def log_response(res):
            f.write(f" Response: {res.status} {res.url}\n")

        page.on("request", log_request)
        page.on("response", log_response)

        with allure.step("Navigate to login page and perform login"):
            login_page.navigate()
            login_page.enter_username()
            login_page.enter_password()
            login_page.click_login()

        with allure.step("Verify successful login by checking dashboard header"):
            assert login_page.dashboard_header.is_visible(), "Login failed - Dashboard not visible"

        with allure.step("Attach network logs to report"):
            allure.attach.file(log_file, name="Network Logs", attachment_type=allure.attachment_type.TEXT)

    print(f"\n Network logs saved to: {log_file}")
