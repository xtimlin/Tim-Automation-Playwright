import pytest
from playwright.sync_api import Browser, BrowserContext, Page
from page_objects.consumer_affairs.home import Home
from page_objects.consumer_affairs.awards import Awards
from page_objects.consumer_affairs.review.write_review import WriteReview


@pytest.mark.skip(reason="Skipping because the website's bot detection system is blocking the test.")
class TestConsumerAffairs:
    @pytest.fixture(autouse=True)
    def setup_method(self, browser: Browser, base_url: str):
        context: BrowserContext = browser.new_context()
        self.page: Page = context.new_page()

        self.home = Home(self.page)
        self.awards = Awards(self.page)
        self.write_review = WriteReview(self.page)

        self.page.goto(base_url)
        self.home.validate_home_page_contents()

        yield {"context": context, "page": self.page}
        context.close()

    def test_open_reward_page(self):
        self.home.go_to_awards()
        self.awards.validate_awards_page_contents()

    def test_open_write_review_page(self):
        self.home.go_to_write_review()
        self.write_review.validate_write_review_page_contents()

    def test_trigger_no_review_error(self):
        self.home.go_to_write_review()
        self.write_review.trigger_review_input_error()
