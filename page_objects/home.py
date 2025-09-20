from .base import BasePage
from playwright.sync_api import Page, expect, Locator


class Home(BasePage):
    title: str = "ConsumerAffairs®: Research. Review. Resolve."

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.reward_btn: Locator = page.locator('.tp-hdr__wrp a:has-text("See The winners")')
        self.write_review_link: Locator = page.locator('.ca-hdr__rev-dsk span:has-text("Write a review")')

    def go_to_awards(self):
        self.reward_btn.click()

    def go_to_write_review(self):
        self.write_review_link.click()

    def validate_home_page_contents(self) -> None:
        expect(self.page).to_have_title(self.title)
        expect(self.reward_btn).to_be_visible()
        expect(self.write_review_link).to_be_visible()
