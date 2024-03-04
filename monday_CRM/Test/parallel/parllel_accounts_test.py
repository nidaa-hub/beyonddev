import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.accounts_page import AccountsPage
from logic.home_page import HomePage
from Utils import generate_string


class ParallelAccountsPageTests(unittest.TestCase):
    VALID_USERS = users.valid_users

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        default_browser = 'firefox'
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.get_driver(browser=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.accounts_Page = AccountsPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.switch_to_environment(environment_name="sales CRM")

    def test_add_account_and_and_delete_it(self):
        print("test_add_account_and_and_delete_it")
        task_name = generate_string.generate_text()
        status = self.accounts_Page.add_new_accounts(task_name)  # Use a unique name to ensure the test is reliable
        self.assertTrue(status, "test_add_account_and_and_delete_it did not succeed")
        status = self.accounts_Page.delete_accounts(task_name)
        self.assertTrue(status, "test_add_account_and_and_delete_it did not succeed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
