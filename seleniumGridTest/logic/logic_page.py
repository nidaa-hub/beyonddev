from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class LogicPage(BasePage):

    INSTAGRAM_CLICK ='//div[@id="icons"]/img[4]'
    MY_SCORE = '//div[3]//header//div[2]/a'
    SEARCH_INPUT = '//div[3]//div[2]//input'
    PAGE_ICON = '//header//div[1]/a'
    PAGE_ADVERTISING = '//div[3]//footer//div[2]//a[4]'

    def __init__(self, driver):
        super().__init__(driver)
        self.search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
        self.my_score = self._driver.find_element(By.XPATH, self.MY_SCORE)
        self.page_icon = self._driver.find_element(By.XPATH, self.PAGE_ICON)
        self.instagram_click = self._driver.find_element(By.XPATH, self.INSTAGRAM_CLICK)
        self.page_advertising = self._driver.find_element(By.XPATH, self.PAGE_ADVERTISING)

    def execute(self):
        return self.driver.title

    def click_on_instagram_button(self):
        self.instagram_click.Click()

    def instagram_button_to_check(self):
        return self.instagram_click

    def click_on_my_score_button(self):
        self.my_score.Click()

    def instagram_button_to_check(self):
        return self.my_score

    def fill_search_input(self, text):
        self.search_input.send_keys(text)

    def press_enter_on_search_input(self):
        self.search_input.send_keys(Keys.RETURN)

    def search_flow(self, text):
        self.fill_search_input(text)
        self.press_enter_on_search_input()

    def click_on_page_icon_button(self):
        self.page_icon.Click()

    def page_icon_button_to_check(self):
        return self.page_icon

    def click_on_advertising_page(self):
        self.page_advertising.Click()

    def page_advertising_button_to_check(self):
        return self.page_advertising

