import pytest
from playwright.sync_api import Browser, BrowserContext, Page
from page_objects.practice_test_automation.home import Home
from page_objects.practice_test_automation.practice import Practice
from page_objects.practice_test_automation.course import Courses
from page_objects.practice_test_automation.test_login import TestLogin


class TestPracticeTestAutomation:
    @pytest.fixture(autouse=True)
    def setup_method(self, browser: Browser, base_url: str):
        context: BrowserContext = browser.new_context()
        self.page: Page = context.new_page()

        self.home = Home(self.page)
        self.practice = Practice(self.page)
        self.courses = Courses(self.page)
        self.login_page = TestLogin(self.page)

        self.page.goto(base_url)
        self.home.validate_home_page_contents()

        yield {"context": context, "page": self.page}
        context.close()

    def test_open_web_practice_page(self):
        self.home.go_to_practice_page()
        self.practice.validate_practice_page_contents()

    def test_open_courses_page(self):
        self.home.go_to_courses_page()
        self.courses.validate_courses_page_contents()

    def test_trigger_error_on_login_page(self):
        self.home.go_to_practice_page()
        self.practice.go_to_test_login_page()
        self.login_page.validate_login_page_contents()
        self.login_page.trigger_error('username', 'password')