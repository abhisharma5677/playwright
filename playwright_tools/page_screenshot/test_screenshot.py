# ---------Environmental SetUp----------
# 1. create a virtual environment    ---> sudo apt-get install python3-venv    ----> python3 -m venv venv
# 2. enter into virtual environment  ----> source venv/bin/activate
# 3. install pytest-playwright plugin   ---> pip install pytest-playwright



import pytest
from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_has_get_started_link(page: Page):

    page.goto("https://playwright.dev/python")

    page.screenshot(path="playwright.jpg")

    link = page.get_by_role("link", name="GET STARTED")
    link.click()
    
    assert page.url == DOCS_URL