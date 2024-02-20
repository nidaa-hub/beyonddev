from selenium import webdriver


class BasePage:
    HUB_URL = 'http://172.20.10.3:4444'

    def __init__(self, driver):
        self.driver = driver
        print("start test: ")

    def get_url_driver(self):
        return self.driver.current_url

