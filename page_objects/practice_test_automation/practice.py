from page_objects.base import BasePage
from playwright.sync_api import Page, expect, Locator


class Practice(BasePage):
    title: str = "Practice | Practice Test Automation"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.test_login_page_link: Locator = page.locator('//a[text()="Test Login Page"]')
        self.test_exceptions_link: Locator = page.locator('//a[text()="Test Exceptions"]')

    def validate_practice_page_contents(self) -> None:
        expect(self.page).to_have_title(self.title)
        expect(self.test_login_page_link).to_be_visible()
        expect(self.test_exceptions_link).to_be_visible()

    def go_to_test_login_page(self):
        self.test_login_page_link.click()
