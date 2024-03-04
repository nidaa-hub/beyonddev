import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.activities_page import ActivitiesPage
from logic.home_page import HomePage


class NonParallelActivitiesPageTests(unittest.TestCase):
    VALID_USERS = users.valid_users

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        default_browser = 'firefox'  # Specify your default browser here
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.get_driver(browser=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.accounts_Page = ActivitiesPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.switch_to_environment(environment_name="sales CRM")

    def test_delete_all_activities_that_have_same_name(self):
        print("test_delete_all_activities_that_have_same_name")
        status = self.accounts_Page.delete_activity("New activity", "all")
        self.assertTrue(status, "test_delete_all_activities_that_have_same_name did not succeed")

    def test_delete_all_activities_and_undo(self):
        print("test_delete_all_activities_and_undo")
        status = self.accounts_Page.undo_delete_all_activities()
        self.assertTrue(status, "test_delete_all_activities_and_undo did not succeed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
