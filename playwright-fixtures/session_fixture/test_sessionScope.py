from playwright.sync_api import *


def page_have_docs_link(
        playwright: Playwright,
        browser: Browser,
        browser_type: BrowserType,
        browserName: str,
        browserChannel: str,
):
    page = browser.new_page()

    # if we have to right browser specific code
    if browser_type == playwright.chromium:
        pass   # right chromium specific code
    elif browser_type == playwright.firefox:
        pass   # write firefox specific code  

    page.goto("https://playwright.dev/python")

    docs_link = page.get_by_role("link" , name="Docs")

    expect(docs_link).to_be_visible()



def test_get_started_visits_docs(browser):
    page = browser.new_page()                           # browser is created once and simply used here

    page.goto("https://playwright.dev/python")

    get_started_link = page.get_by_role("link" , name="GET STARTED")

    get_started_link.click()

    expect(page).to_have_url("https://playwright.dev/python/docs/intro")










# #  Better way of writting browser specific code
# import pytest
# from playwright.sync_api import *

# @pytest.mark.skip_browser("firefox")           # this test is not for firefox browser
# def page_have_docs_link(page : Page):
#     page.goto("https://playwright.dev/python")

#     docs_link = page.get_by_role("link" , name="Docs")

#     expect(docs_link).to_be_visible()


# @pytest.mark.only_browser("firefox")           # this test is only for firefox browser
# def test_get_started_visits_docs(page : Page):
#     page.goto("https://playwright.dev/python")

#     get_started_link = page.get_by_role("link" , name="GET STARTED")

#     get_started_link.click()

#     expect(page).to_have_url("https://playwright.dev/python/docs/intro")

