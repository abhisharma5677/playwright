import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(autouse=True)
def visit_test_page(page: Page):
    page.goto("https://github.com/login")


def test_successful_login(page: Page):
    email = "imabhishek5677@gmail.com"
    password = "arpitasharma5677"
    url = "https://github.com/"


    email_input = page.get_by_label("Username or email address")
    password_input = page.get_by_label("Password")
    btn = page.query_selector('.js-sign-in-button')


    email_input.fill(email)
    password_input.fill(password)
    btn.click()


    profile_button = page.query_selector('button[aria-label="Open user account menu"]')
    profile_button.click()

    assert page.url == url

    print("Page Url matched with expected url")



