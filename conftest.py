import pytest
from playwright.sync_api import sync_playwright
from datetime import datetime
import os

# Absolute path to repo root
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STORAGE_FILE = os.path.join(PROJECT_ROOT, "storage_state.json")

# STORAGE_FILE = "storage_state.json"


@pytest.fixture(scope="session", params=["chromium"])
def browser(request):
    playwright = sync_playwright().start()
    browser_type = getattr(playwright, request.param)   # dynamically pick browser type
    browser = browser_type.launch(headless=False, slow_mo=500)
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def context(browser, request):
    # Always reuse storage state (skip login)
    if not os.path.exists(STORAGE_FILE):
        raise RuntimeError(
            f"{STORAGE_FILE} not found. Run utils/create_storage_state.py first."
        )

    context = browser.new_context(storage_state=STORAGE_FILE)

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context

    rep_call = getattr(request.node, "rep_call", None)

    try:
        # Save trace only if test failed
        if rep_call and rep_call.failed:
            os.makedirs("traces", exist_ok=True)
            trace_path = (
                f"traces/{request.node.name}_"
                f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.zip"
            )
            context.tracing.stop(path=trace_path)
            print(f"\n Trace saved: {trace_path}")
        else:
            context.tracing.stop()
    except Exception as e:
        print(f"\n[Warning] Error while stopping trace: {e}")

    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    yield page


# Hook to know test outcome (so we know if failed inside fixture)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
