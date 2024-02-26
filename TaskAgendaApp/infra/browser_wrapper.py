from selenium import webdriver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName="Android",
    deviceName="emulator-5554",
    platformVersion="11.0",
    automationName="UiAutomator2",
    appPackage="com.claudivan.taskagenda",
    appActivity=".Activities.MainActivity"
)

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


class BrowserWrapper:

    def __init__(self):
        self.driver = None
        print("test start")

    def get_driver(self):
        self.driver = webdriver.Remote(
            command_executor=appium_server_url,
            options=capabilities_options
        )
        return self.driver

