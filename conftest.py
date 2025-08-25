import pytest
from playwright.sync_api import sync_playwright
from datetime import datetime
import os

STORAGE_FILE = "storage_state.json"


@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=500)  # fixed to chromium
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def context(browser, request):
    # Reuse saved storage state if available
    if os.path.exists(STORAGE_FILE):
        context = browser.new_context(storage_state=STORAGE_FILE)
    else:
        context = browser.new_context()

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context

    # Save storage state after login test (first time)
    if "login" in request.node.name.lower() and not os.path.exists(STORAGE_FILE):
        context.storage_state(path=STORAGE_FILE)
        print(f"\n Storage state saved to {STORAGE_FILE}")

    # If test failed, save the trace
    if request.node.rep_call.failed:
        os.makedirs("traces", exist_ok=True)
        trace_path = f"traces/{request.node.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.zip"
        context.tracing.stop(path=trace_path)
        print(f"\n Trace saved: {trace_path}")
    else:
        context.tracing.stop()

    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page


# Hook to know test outcome (so we know if failed inside fixture)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
