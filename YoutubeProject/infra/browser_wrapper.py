from selenium import webdriver

class BrowserWrapper:

    def __init__(self):
        self.driver = None
        print("test start")

    def get_driver(self, url):
        self.driver = webdriver.Chrome("C:\\Users\\nidaa\\PycharmProjects\\ExampleProject\\chromedriver.exe")
        self.driver.get(url)
        return self.driver

