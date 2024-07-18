from playwright.sync_api import Page


class NoteCardViewPage:
    def __init__(self, page: Page):
        self.page = page
        self.note_card_title = page.get_by_test_id("note-card-title")
        self.note_card_description = page.get_by_test_id("note-card-description")
        self.note_card_completed_checkbox = page.get_by_test_id("toggle-note-switch")
        self.note_card_edit_btn = page.get_by_test_id("note-edit")
        self.note_card_delete_btn = page.get_by_test_id("note-delete")
        self.delete_confirm_btn = page.get_by_test_id("note-delete-confirm")