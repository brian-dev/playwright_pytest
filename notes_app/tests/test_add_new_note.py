import pytest

from playwright.sync_api import Page
from notes_app.pages.home_page import HomePage
from notes_app.pages.login_page import LoginPage
from notes_app.pages.note_card_view_page import NoteCardViewPage
from notes_app.pages.welcome_page import WelcomePage
from notes_app import props
from notes_app.utils.generators import Generators

generator = Generators()
note_types = ['Home', 'Work', 'Personal']


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    wp = WelcomePage(page)
    lp = LoginPage(page)

    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(props['urls']['base_url'])
    wp.click_login_btn()
    lp.login('default')

    yield
    print("Test is complete")


def test_add_new_note(page: Page):
    hp = HomePage(page)
    title = generator.generate_random_str()
    description = generator.generate_random_str()

    for note_type in note_types:
        hp.create_new_note(note_type, title, description)

        assert page.get_by_test_id("note-card-title").inner_text() == title

        hp.note_card_delete_btn.click()
        hp.delete_confirm_btn.click()


def test_note_card_elements(page: Page):
    hp = HomePage(page)
    title = generator.generate_random_str()
    description = generator.generate_random_str()

    for note_type in note_types:
        hp.create_new_note(note_type, title, description)

        assert page.get_by_test_id("note-card-title").inner_text() == title
        assert page.get_by_test_id("note-card-description").inner_text() == f"{description}\n"
        assert hp.note_card_completed_checkbox.is_visible()
        assert hp.note_card_view_btn.is_visible()
        assert hp.note_card_delete_btn.is_visible()
        assert hp.note_card_edit_btn.is_visible()

        hp.note_card_delete_btn.click()
        hp.delete_confirm_btn.click()


def test_view_note_card(page: Page):
    hp = HomePage(page)
    vp = NoteCardViewPage(page)
    title = generator.generate_random_str()
    description = generator.generate_random_str()

    hp.create_new_note('Home', title, description)
    hp.note_card_view_btn.click()
    assert vp.note_card_title.inner_text() == title
    assert vp.note_card_description.inner_text() == f"{description}\n"

    vp.note_card_delete_btn.click()
    vp.delete_confirm_btn.click()


def test_edit_note_card(page: Page):
    hp = HomePage(page)
    title = generator.generate_random_str()
    description = generator.generate_random_str()

    hp.create_new_note('Home', title, description)
    hp.note_card_edit_btn.click()

    page.wait_for_selector('.modal-title')
    assert page.get_by_text('Edit note').is_visible()

    hp.cancel_new_note_btn.click()
    hp.note_card_delete_btn.click()
    hp.delete_confirm_btn.click()


def test_add_completed_card(page: Page):
    hp = HomePage(page)
    title = generator.generate_random_str()
    description = generator.generate_random_str()

    for note_type in note_types:
        hp.create_new_note(note_type, title, description, completed=True)

        assert hp.note_card_completed_checkbox.is_checked()

        hp.note_card_delete_btn.click()
        hp.delete_confirm_btn.click()


def test_long_title(page: Page):
    hp = HomePage(page)
    title = generator.generate_random_str(num_chars=110, auto_generate=False)
    description = generator.generate_random_str()

    hp.create_new_note('Home', title, description)

    assert page.get_by_text('Title should be between 4 and 100 characters').is_visible()


def test_short_title(page: Page):
    hp = HomePage(page)
    title = generator.generate_random_str(num_chars=3, auto_generate=False)
    description = generator.generate_random_str()

    hp.create_new_note('Home', title, description)

    assert page.get_by_text('Title should be between 4 and 100 characters').is_visible()


def test_long_description(page: Page):
    hp = HomePage(page)
    title = generator.generate_random_str()
    description = generator.generate_random_str(num_chars=1005, auto_generate=False)

    hp.create_new_note('Home', title, description)

    assert page.get_by_text('Description should be between 4 and 1000 characters').is_visible()


def test_short_description(page: Page):
    hp = HomePage(page)
    title = generator.generate_random_str()
    description = generator.generate_random_str(num_chars=2, auto_generate=False)

    hp.create_new_note('Home', title, description)

    assert page.get_by_text('Description should be between 4 and 1000 characters').is_visible()


def test_empty_title(page: Page):
    hp = HomePage(page)
    title = ''
    description = generator.generate_random_str()

    hp.create_new_note('Home', title, description)

    assert page.get_by_text('Title is required').is_visible()


def test_empty_description(page: Page):
    hp = HomePage(page)
    title = generator.generate_random_str()
    description = ''

    hp.create_new_note('Home', title, description)

    assert page.get_by_text('Description is required')


def test_empty_title_and_description(page: Page):
    hp = HomePage(page)
    title = ''
    description = ''

    hp.create_new_note('Home', title, description)

    assert page.get_by_text('Title is required').is_visible() and page.get_by_text('Description is required').is_visible()


def test_cancel_new_note(page: Page):
    hp = HomePage(page)
    title = generator.generate_random_str()
    description = generator.generate_random_str()

    hp.add_note_btn.click()
    hp.create_note_title_input.fill(title)
    hp.create_note_description_input.fill(description)
    hp.cancel_new_note_btn.click()

    assert page.get_by_text('You don\'t have any notes in all categories').is_visible()
