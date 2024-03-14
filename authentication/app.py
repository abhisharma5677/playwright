from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.firefox.launch(headless=False , slow_mo=1000)

    # create browser context
    context = browser.new_context()

    # create  a new page
    page = context.new_page()

    # visit the google login website
    page.goto("https://accounts.google.com")


    #fill email for the google login
    email_input = page.get_by_label("Email or Phone")
    email_input.fill("imabhishek5677@gmail.com")
    page.get_by_role("button", name="Next").click()


    # fill password for google login
    password_input = page.get_by_label("Enter your password")
    password_input.fill("your password")
    page.get_by_role("button", name="Next").click()


    page.pause()


    # Save authentication state
    context.storage_state(
        path="playwright/.auth/storage_state.json",
    )

    context.close()