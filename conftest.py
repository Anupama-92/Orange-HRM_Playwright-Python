import pytest
from playwright.sync_api import sync_playwright
from datetime import datetime


@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=500)  # fixed to chromium
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = f"screenshots/{item.name}_{timestamp}.png"
            page.screenshot(path=screenshot_path)
            print(f"\n Screenshot saved: {screenshot_path}")
