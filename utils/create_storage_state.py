from playwright.sync_api import sync_playwright

STORAGE_FILE = "storage_state.json"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Manual login once
    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button[type='submit']")

    page.wait_for_url("**/dashboard/**", timeout=20000)

    context.storage_state(path=STORAGE_FILE)
    print(f"Storage state saved to {STORAGE_FILE}")

    browser.close()
