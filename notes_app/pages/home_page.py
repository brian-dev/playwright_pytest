from playwright.sync_api import Page
from notes_app.utils.generators import Generators


class HomePage:
    generators = Generators()

    def __init__(self, page: Page):
        self.page = page
        self.home_btn = page.get_by_test_id("home")
        self.profile_btn = page.get_by_test_id("profile")
        self.logout_btn = page.get_by_test_id("logout")
        self.search_input_field = page.get_by_test_id("search-input")
        self.search_btn = page.get_by_test_id("search-btn")
        self.all_category_btn = page.get_by_test_id("category-all")
        self.home_category_btn = page.get_by_test_id("category-home")
        self.work_category_btn = page.get_by_test_id("category-work")
        self.personal_category_btn = page.get_by_test_id("category-personal")
        self.add_note_btn = page.get_by_test_id("add-new-note")
        self.note_category_select = page.get_by_test_id("note-category")
        self.create_note_title_input = page.get_by_test_id("note-title")
        self.create_note_description_input = page.get_by_test_id("note-description")
        self.create_note_completed_checkbox = page.get_by_test_id("note-completed")
        self.create_new_note_btn = page.get_by_test_id("note-submit")
        self.cancel_new_note_btn = page.get_by_test_id("note-cancel")
        self.note_card_completed_checkbox = page.get_by_test_id("toggle-note-switch")
        self.note_card_view_btn = page.get_by_test_id("note-view")
        self.note_card_edit_btn = page.get_by_test_id("note-edit")
        self.note_card_delete_btn = page.get_by_test_id("note-delete")
        self.delete_confirm_btn = page.get_by_test_id("note-delete-confirm")
        self.delete_cancel_btn = page.get_by_test_id("note-delete-cancel-2")
        self.edit_modal_title = page.query_selector('.modal-title')

    def create_new_note(self, category, title, description, completed=False):
        self.add_note_btn.click()
        self.select_category(category)
        self.create_note_title_input.fill(title)
        self.create_note_description_input.fill(description)
        if completed:
            self.create_note_completed_checkbox.check()
        self.create_new_note_btn.click()

    def select_category(self, category):
        self.page.select_option('#category', value=category)
