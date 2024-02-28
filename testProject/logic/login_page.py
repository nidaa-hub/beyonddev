from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.util import wait

from infra.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_INPUT = '//button[contains(text(), "Login")]'
    PASSWORD_INPUT = '//body//div[2]//div[1]//div[2]//input'

    def __init__(self, driver):
        super().__init__(driver)
        self.login_input = self.wait.until(EC.visibility_of_element_located(By.XPATH, self.LOGIN_INPUT))
        self.Password_input = self.wait.until(EC.visibility_of_element_located(By.XPATH, self.PASSWORD_INPUT))

    def fill_login_input_text_on_monday_website(self, email):
        self.login_input.send_keys(email)

    def press_enter_on_login_input(self):
        self.login_input.send_keys(Keys.RETURN)

    def login_flow_for_monday_website(self, email):
        self.fill_login_input_text_on_monday_website(email)
        self.press_enter_on_login_input()

    def fill_password_input_text_on_monday_website(self, password):
        self.Password_input.send_keys(password)

    def press_enter_on_password_input(self):
        self.Password_input.send_keys(Keys.RETURN)

    def password_flow_for_monday_website(self, password):
        self.fill_password_input_text_on_monday_website(password)
        self.press_enter_on_password_input()





