from playwright.sync_api import Page


class WelcomePage:
    def __init__(self, page: Page):
        self.page = page
        self.login_btn = page.locator('a[href="/notes/app/login"]')
        self.register_btn = page.get_by_test_id("open-register-view")
        self.forgot_password_btn = page.get_by_test_id("forgot-password-view")

    def click_login_btn(self):
        self.login_btn.click()

    def click_register_btn(self):
        self.register_btn.click()

    def click_forgot_password_btn(self):
        self.forgot_password_btn.click()
