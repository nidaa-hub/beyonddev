import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.activities_page import ActivitiesPage
from logic.home_page import HomePage
from Utils import generate_string


class ParallelActivitiesPageTests(unittest.TestCase):
    VALID_USERS = users.valid_users

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        default_browser = 'firefox'
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.get_driver(browser=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.activities_Page = ActivitiesPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.switch_to_environment(environment_name="sales CRM")

    def test_add_activity_and_and_delete_it(self):
        print("test_add_activity_and_and_delete_it")
        task_name = generate_string.generate_text()
        status = self.activities_Page.add_new_activity(task_name)
        self.assertTrue(status, "test_add_activity_and_and_delete_it did not succeed")
        status = self.activities_Page.delete_activity(task_name)
        self.assertTrue(status, "test_add_activity_and_and_delete_it did not succeed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
