from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class HomePage(BasePage):

    STARTED_INPUT = "//body//div[2]//header//nav/div[1]/div/div[1]"
    LOGIN_BUTTON = "//div[2]//header//nav//div[3]/a"

    def __init__(self, driver):
        super().__init__(driver)
        self.get_started_button = self._driver.find_element(By.XPATH, self.STARTED_INPUT)
        self.login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)

    def click_on_get_started_button(self):
        self.get_started_button.click()

    def click_on_login_button_on_monday_website(self):
        self.login_button.click()
