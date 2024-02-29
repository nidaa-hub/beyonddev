from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class PasswordPage(BasePage):

    PASSWORD_INPUT = '//input[@id="user_password"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.Password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)

    def fill_password_input_text_on_monday_website(self, password):
        self.Password_input.send_keys(password)

    def press_enter_on_password_input(self):
        self.Password_input.send_keys(Keys.RETURN)

    def password_flow_for_monday_website(self, password):
        self.fill_password_input_text_on_monday_website(password)
        self.press_enter_on_password_input()