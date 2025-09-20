from .base import BasePage
from playwright.sync_api import Page, expect, Locator


class Awards(BasePage):
    title: str = "Buyer’s Choice Awards | ConsumerAffairs®"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.content_title: Locator = page.locator('h2:has-text("Check out our winners")')

    def validate_awards_page_contents(self) -> None:
        expect(self.page).to_have_title(self.title)
        expect(self.content_title).to_be_visible()
