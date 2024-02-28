from selenium import webdriver

class BrowserWrapper:

    def __init__(self):
        self.driver = None
        print("test start")

    def get_driver(self, url):
        print("get driver step1")
        self.driver = webdriver.Chrome()
        print("get driver step2")
        self.driver.get(url)
        print("get driver step3")
        return self.driver
