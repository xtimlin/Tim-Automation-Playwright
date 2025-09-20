from page_objects.base import BasePage
from playwright.sync_api import Page, expect, Locator


class Courses(BasePage):
    title: str = "Courses | Practice Test Automation"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.header: Locator = page.locator('//h1[text()="Courses"]')

    def validate_courses_page_contents(self) -> None:
        expect(self.page).to_have_title(self.title)
        expect(self.header).to_be_visible()
