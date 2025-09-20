from page_objects.base import BasePage
from playwright.sync_api import Page, expect, Locator


class TestLogin(BasePage):
    title: str = "Test Login | Practice Test Automation"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username_input: Locator = page.locator('#username')
        self.password_input: Locator = page.locator('#password')
        self.submit_btn: Locator = page.locator('#submit')
        self.error_msg: Locator = page.locator("#error", has_text="Your username is invalid!")

    def validate_login_page_contents(self) -> None:
        expect(self.page).to_have_title(self.title)
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.submit_btn).to_be_visible()

    def trigger_error(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_btn.click()
        expect(self.error_msg).to_be_visible(timeout=2)
