import os

from playwright.sync_api import Page
from notes_app import props
from dotenv import load_dotenv

load_dotenv()


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_test_id("login-email")
        self.password_input = page.get_by_test_id("login-password")
        self.login_button = page.get_by_test_id("login-submit")
        self.forgot_password_btn = page.get_by_test_id("forgotPasswordLink")

    def login(self, user_type):
        if user_type == "default":
            self.username_input.fill(os.getenv('EMAIL'))
            self.password_input.fill(os.getenv('PASS'))
        else:
            self.username_input.fill(props['login_users'][user_type]['username'])
            self.password_input.fill(props['login_users'][user_type]['password'])

        self.login_button.click()
