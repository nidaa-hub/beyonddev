import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.password_page import PasswordPage


class MondayTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        print("i'm stock here")
        self.driver = self.browser.get_driver("http://www.monday.com/")
        print("lets go")
        #self.started_monday = HomePage(self.driver)
        #self.login_monday = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_get_started(self):
        self.started_monday = HomePage(self.driver)
        self.started_monday.click_on_get_started_button()
        time.sleep(5)

    def test_sign_in_monday_website(self):
        self.started_monday = HomePage(self.driver)
        self.started_monday.click_on_login_button_on_monday_website()
        time.sleep(3)
        self.login_monday = LoginPage(self.driver)
        self.login_monday.login_flow_for_monday_website("gethelpproject2021@gmail.com")
        time.sleep(3)
        self.password_monday = PasswordPage(self.driver)
        self.password_monday.password_flow_for_monday_website("gethelp24")
        time.sleep(3)







