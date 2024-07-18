import time

from playwright.sync_api import Page
from notes_app import props
from notes_app.pages import generators


class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("input[data-testid='register-email']")
        self.password_input = page.locator("input[data-testid='register-password']")
        self.name_input = page.locator("input[data-testid='register-name']")
        self.password2_input = page.locator("input[data-testid='register-confirm-password']")
        self.register_btn = page.locator("button[data-testid='register-submit']")
        self.register_success_login_btn = page.locator("a[data-testid='login-view")

    def register(self, data_type='default', auto_generate=False):
        if auto_generate and data_type == 'default':
            email = f"{generators.generate_random_str()}@example.com"
            password = f"{generators.generate_mixed_str()}"
            password2 = password
            name = f"{generators.generate_random_str()}"
        elif data_type == 'mismatched_password' or data_type == 'empty_password':
            email = props['registration_users'][data_type]['email']
            password = props['registration_users'][data_type]['password']
            password2 = props['registration_users'][data_type]['password2']
            name = props['registration_users'][data_type]['name']
        else:
            email = props['registration_users'][data_type]['email']
            password = props['registration_users'][data_type]['password']
            password2 = password
            name = props['registration_users'][data_type]['name']

        self.email_input.fill(email)
        self.password_input.fill(password)
        self.name_input.fill(name)
        self.password2_input.fill(password2)
        self.register_btn.click()
        time.sleep(1.0)

    def register_success_login(self):
        self.register_success_login_btn.click()
