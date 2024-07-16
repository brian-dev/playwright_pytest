import pytest

from playwright.sync_api import Page
from notes_app.pages.register_page import RegisterPage
from notes_app import props


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(props['urls']['register_url'])
    yield
    print("Test is complete")


def test_create_new_user(page: Page):
    rp = RegisterPage(page)

    if page.url != props['urls']['register_url']:
        page.goto(props['urls']['register_url'])

    rp.register(auto_generate=True)
    assert page.get_by_text("User account created successfully").is_visible()


def test_create_existing_user(page: Page):
    rp = RegisterPage(page)

    if page.url != props['urls']['register_url']:
        page.goto(props['urls']['register_url'])

    rp.register(data_type='registered_user')
    assert page.get_by_text("An account already exists with the same email address").is_visible()


def test_invalid_email(page: Page):
    rp = RegisterPage(page)

    if page.url != props['urls']['register_url']:
        page.goto(props['urls']['register_url'])

    rp.register(data_type='invalid_email')
    assert page.get_by_text("Email address is invalid").is_visible()


def test_empty_email(page: Page):
    rp = RegisterPage(page)

    if page.url != props['urls']['register_url']:
        page.goto(props['urls']['register_url'])

    rp.register(data_type='empty_email')
    assert page.get_by_text("Email address is required").is_visible()


def test_short_password(page: Page):
    rp = RegisterPage(page)

    if page.url != props['urls']['register_url']:
        page.goto(props['urls']['register_url'])

    rp.register(data_type='short_password')
    assert page.get_by_text("Password should be between 6 and 30 characters").is_visible()


def test_long_password(page: Page):
    rp = RegisterPage(page)

    if page.url != props['urls']['register_url']:
        page.goto(props['urls']['register_url'])

    rp.register(data_type='long_password')
    assert page.get_by_text("Password should be between 6 and 30 characters").is_visible()


def test_empty_password(page: Page):
    rp = RegisterPage(page)

    if page.url != props['urls']['register_url']:
        page.goto(props['urls']['register_url'])

    rp.register(data_type='empty_password')
    assert page.get_by_text("Password is required").is_visible()


def test_mismatched_password(page: Page):
    rp = RegisterPage(page)

    if page.url != props['urls']['register_url']:
        page.goto(props['urls']['register_url'])

    rp.register(data_type='mismatched_password')
    assert page.get_by_text("Passwords don't match!").is_visible()


def test_short_name(page: Page):
    rp = RegisterPage(page)

    if page.url != props['urls']['register_url']:
        page.goto(props['urls']['register_url'])

    rp.register(data_type='short_name')
    assert page.get_by_text("User name should be between 4 and 30 characters").is_visible()


def test_long_name(page: Page):
    rp = RegisterPage(page)

    if page.url != props['urls']['register_url']:
        page.goto(props['urls']['register_url'])

    rp.register(data_type='long_name')
    assert page.get_by_text("User name should be between 4 and 30 characters").is_visible()


def test_empty_name(page: Page):
    rp = RegisterPage(page)

    if page.url != props['urls']['register_url']:
        page.goto(props['urls']['register_url'])

    rp.register(data_type='empty_name')
    assert page.get_by_text("User name is required").is_visible()
