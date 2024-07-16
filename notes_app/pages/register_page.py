from playwright.sync_api import Page
# from notes_app.utils.generators import Generators
from notes_app.pages import generators


class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("input[data-testid='register-email']")
        self.password_input = page.locator("input[data-testid='register-password']")
        self.name_input = page.locator("input[data-testid='register-name']")
        self.password2_input = page.locator("input[data-testid='register-confirm-password']")
        self.register_btn = page.locator("button[data-testid='register-submit']")
        self.register_success_div = page.locator("div[class='alert-success']")
        self.register_success_login_btn = page.locator("a[data-testid='login-view")

    def register(self):
        # string_generator = Generators()

        email = f"{generators.generate_random_str()}@example.com"
        password = f"{generators.generate_mixed_str()}"
        name = f"{generators.generate_random_str()}"

        self.email_input.fill(email)
        self.password_input.fill(password)
        self.name_input.fill(name)
        self.password2_input.fill(password)
        self.register_btn.click()

    def register_success_login(self):
        self.register_success_login_btn.click()

    def success_div_visible(self):
        return self.register_success_div.is_visible()
