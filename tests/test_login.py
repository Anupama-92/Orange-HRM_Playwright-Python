import pytest
import allure
import os
from pages.login_page import LoginPage


@pytest.mark.login
def test_valid_login(page, request):
    login_page = LoginPage(page)
    # Define log file path (one per test run)
    log_file = os.path.join(os.getcwd(), f"network_logs_{request.node.name}.txt")
    # Open file in write mode
    with open(log_file, "w", encoding="utf-8") as f:
        # Capture request logs
        def log_request(req):
            f.write(f" Request: {req.method} {req.url}\n")

        # Capture response logs
        def log_response(res):
            f.write(f" Response: {res.status} {res.url}\n")
        # Attach event listeners
        page.on("request", log_request)
        page.on("response", log_response)
        # Perform login
        login_page.navigate()
        login_page.enter_username()
        login_page.enter_password()
        login_page.click_login()
        # Assertion
        assert login_page.dashboard_header.is_visible(), "Login failed - Dashboard not visible"
    print(f"\n Network logs saved to: {log_file}")