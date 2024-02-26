import time
from selenium.webdriver.common.by import By

from infra.base_page import BasePageApp

class MenuPage(BasePageApp):
    MENU_BUTTON = 'com.claudivan.taskagenda:id/hamburguer'
    SETTING_BUTTON = '//android.widget.RelativeLayout[@resource-id="com.claudivan.taskagenda:id/btAjustes"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.menu = self.driver.find_element(By.ID, value=self.MENU_BUTTON)
        self.setting = self.driver.find_element(By.XPATH, value=self.SETTING_BUTTON)

    def click_on_menu_button(self):
        self.menu.click()
        return self.menu

    def click_on_setting_button(self):
        self.setting.click()
        return self.setting

    def dark_mode_app(self):
        self.menu.click_on_menu_button()
        time.sleep(3)
        self.setting.click_on_setting_button()
        return self.setting
