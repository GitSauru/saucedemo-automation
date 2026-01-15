import pytest
from playwright.sync_api import sync_playwright
from pages.login import LoginPage
from utils.creds import username, password, url



@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False, slow_mo= 600)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    yield page
    context.close()


@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.login_page(username, password)
    yield page

    


