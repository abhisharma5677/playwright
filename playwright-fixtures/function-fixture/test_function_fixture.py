
from playwright.sync_api import *



def page_have_docs_link(page : Page):
    page.goto("https://playwright.dev/python")

    docs_link = page.get_by_role("link" , name="Docs")

    expect(docs_link).to_be_visible()



def test_get_started_visits_docs(page : Page):
    page.goto("https://playwright.dev/python")

    get_started_link = page.get_by_role("link" , name="GET STARTED")

    get_started_link.click()

    expect(page).to_have_url("https://playwright.dev/python/docs/intro")







