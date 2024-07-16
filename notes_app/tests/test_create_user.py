import time

import pytest

from playwright.sync_api import Page, expect
from notes_app.pages.welcome_page import WelcomePage
from notes_app.pages.register_page import RegisterPage
from notes_app import props


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(props['urls'][0]['base_url'])
    yield
    print("Test is complete")


def test_create_user(page: Page):
    wp = WelcomePage(page)
    rp = RegisterPage(page)

    wp.click_register_btn()
    if page.url != props['urls'][0]['register_url']:
        page.goto(props['urls'][0]['register_url'])
    rp.register()

    time.sleep(0.5)
    assert page.get_by_text("User account created successfully").is_visible()
