from page_objects.base import BasePage
from playwright.sync_api import Page, expect, Locator


class WriteReview(BasePage):
    title: str = "Write a review today"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.header: Locator = page.locator('p:has-text("Share Your Experience")')

        self.review_input: Locator = page.locator('#description-step-0')
        self.review_input_error: Locator = page.locator('label[for="description-step-0"] ~ ul.ca-form__error')

        self.review_title_input: Locator = page.locator('#title-step-0')
        self.review_title_error: Locator = page.locator('label[for="title-step-0"] ~ ul.ca-form__error')

    def validate_write_review_page_contents(self) -> None:
        expect(self.page).to_have_title(self.title)

        expect(self.header).to_be_visible()
        expect(self.review_input).to_be_visible()
        expect(self.review_input_error).not_to_be_visible()
        expect(self.review_title_input).to_be_visible()
        expect(self.review_title_error).not_to_be_visible()

    def trigger_review_input_error(self) -> None:
        self.validate_write_review_page_contents()

        self.review_input.click(delay=100)
        self.review_title_input.click(delay=100)
        self.review_input.type('input size less than 200', delay=100)
        self.review_title_input.click(delay=100)
        self.review_input.click(delay=100)
        self.header.click(delay=100)

        expect(self.review_input_error).to_be_visible(timeout=5)
        expect(self.review_title_error).to_be_visible(timeout=5)
