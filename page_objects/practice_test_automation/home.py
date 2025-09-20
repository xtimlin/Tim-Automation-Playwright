from page_objects.base import BasePage
from playwright.sync_api import Page, expect, Locator


class Home(BasePage):
    title: str = "Practice Test Automation | Learn Selenium WebDriver"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.practice_btn: Locator = page.locator('//a[text()="Practice"]')
        self.courses_btn: Locator = page.locator('//a[text()="Courses"]')

    def go_to_practice_page(self):
        self.practice_btn.click()

    def go_to_courses_page(self):
        self.courses_btn.click()

    def validate_home_page_contents(self) -> None:
        expect(self.page).to_have_title(self.title)
        expect(self.practice_btn).to_be_visible()
        expect(self.courses_btn).to_be_visible()
