import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.contacts_page import ContactsPage
from logic.home_page import HomePage
from Utils import generate_string


class ParallelContactsPageTests(unittest.TestCase):
    VALID_USERS = users.valid_users

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        default_browser = 'firefox'
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.get_driver(browser=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.contacts_Page = ContactsPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.switch_to_environment(environment_name="sales CRM")

    def test_add_contacts_and_and_delete_it(self):
        print("test_add_leads_and_and_delete_it")
        task_name = generate_string.generate_text()
        status = self.contacts_Page.add_new_contacts(task_name)
        self.assertTrue(status, "test_add_leads_and_and_delete_it did not succeed")
        status = self.contacts_Page.delete_contacts(task_name)
        self.assertTrue(status, "test_add_leads_and_and_delete_it did not succeed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
