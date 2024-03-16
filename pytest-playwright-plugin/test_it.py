# ---------Environmental SetUp----------
# 1. create a virtual environment    ---> sudo apt-get install python3-venv    ----> python3 -m venv venv
# 2. enter into virtual environment  ----> source venv/bin/activate
# 3. install pytest-playwright plugin   ---> pip install pytest-playwright




# Writting a test using pytest-playwright plugin to test if the url of the visited page is matching Expected url


# ---------- first way------------------

# import pytest
# from playwright.sync_api import Page

# DOCS_URL = "https://playwright.dev/python/docs/intro"


# # Common code used by both tests in the starting.......
# @pytest.fixture
# def playwright_page(page: Page):
#     page.goto("https://playwright.dev/python")
#     return page


# def test_page_has_docs_link(playwright_page: Page):
#     link = playwright_page.get_by_role("link", name="Docs")
#     assert link.is_visible()


# def test_get_started_visits_docs(playwright_page: Page):
#     link = playwright_page.get_by_role("link", name="GET STARTED")
#     link.click()

#     assert playwright_page.url == DOCS_URL







# ---------2nd way--------------

import pytest
from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"

#  Common code used by both the tests....autouse = True ()
@pytest.fixture(autouse=True, scope="function")
def visit_playwright(page: Page):
    # setup
    page.goto("https://playwright.dev/python")
   
    # yield value and pause
    yield page                 # "yield" is used to perform some action before test function and some action after test function
   
    # teardown
    page.close()
    print("\n[ Fixture ]: page closed!")


def test_page_has_docs_link(page: Page):
    link = page.get_by_role("link", name="Docs")
    assert link.is_visible()


def test_get_started_visits_docs(page: Page):
    link = page.get_by_role("link", name="GET STARTED")
    link.click()

    assert page.url == DOCS_URL











# -------------for Running test----------------
#  1. pytest   
    #  ----> simply running the test (done using pytest-playwright plugin)

#  2. pytest --headed      
    # -----> if we want to see the user interface on the browser during test (done using pytest-playwright plugin) 

#  3. pytest --headed --slowmo=500  
    # -----> to slow down the testing speed 

#  4. pytest --headed --browser=firefox   
    # ----> specify the browser for the test(done using pytest-playwright plugin)  ---> by default chromium browser







# ------------pytest config file-------------
#  always named as "pytest.ini"
#  pytest   ----> runs the command specified in pytest config file 