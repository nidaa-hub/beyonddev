from selenium import webdriver


class BrowserWrapper:

    HUB_URL = 'http://172.20.10.3:4444'

    def __init__(self):
        self.driver = None

    def get_driver(self, cap):
        self.driver = webdriver.Remote(command_executor=self.HUB_URL, options=cap)
        self.driver.get("https://www.365scores.com/he")
        return self.driver




