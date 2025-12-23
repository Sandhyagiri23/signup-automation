from playwright.sync_api import Playwright, sync_playwright
import time 
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://authorized-partner.vercel.app/register")
    page.get_by_role("checkbox", name="I agree to the Terms of").click()
    page.get_by_role("button", name="Continue").click()
    


    page.wait_for_selector("input[placeholder*='First']")

    page.fill("input[name='firstName']", "Sandhya")
    page.fill("input[name='lastName']", "Giri")

    unique_email = f"qa_{int(time.time())}@example.com"
    page.fill("input[name='email']", unique_email)
    

    page.fill("input[name='phoneNumber']", "9869999999")
    page.fill("input[name='password']", "Spassword123!")
    page.fill("input[name='confirmPassword']", "Spassword123!")

    page.get_by_role("button", name="Next").click()

    page.wait_for_timeout(5000)
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
