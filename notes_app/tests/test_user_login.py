import pytest

from playwright.sync_api import Page
from notes_app import props
from notes_app.pages.home_page import HomePage
from notes_app.pages.login_page import LoginPage


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(props['urls']['login_url'])
    yield
    print("Test is complete")


def test_incorrect_username(page: Page):
    lp = LoginPage(page)

    lp.login('incorrect_username')
    assert page.get_by_text("Incorrect email address or password").is_visible()


def test_incorrect_password(page: Page):
    lp = LoginPage(page)

    lp.login('incorrect_password')
    assert page.get_by_text("Incorrect email address or password").is_visible()


def test_empty_username(page: Page):
    lp = LoginPage(page)

    lp.login('empty_username')
    assert page.get_by_text("Email address is required").is_visible()


def test_empty_password(page: Page):
    lp = LoginPage(page)

    lp.login('empty_password')
    assert page.get_by_text("Password is required").is_visible()


def test_empty_credentials(page: Page):
    lp = LoginPage(page)

    lp.login_button.click()
    assert page.get_by_text("Email address is required").is_visible() and page.get_by_text("Password is required")


def test_valid_login(page: Page):
    lp = LoginPage(page)
    hp = HomePage(page)

    lp.login('default')
    page.wait_for_load_state("load")
    assert hp.home_btn.is_visible()
