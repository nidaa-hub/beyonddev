import time
from selenium.webdriver.common.by import By
from infra.base_page import BasePageApp


class Calender(BasePageApp):
    ADD_BUTTON = 'com.claudivan.taskagenda:id/btNovoEvento'
    TODAY_SCHEDULE = 'com.claudivan.taskagenda:id/containerColunasHorarios'
    TOMORROW_BUTTON = '//android.widget.TextView[@resource-id="android:id/text1" and @text="Tomorrow"'
    NEXT_WEEK = '//android.widget.ImageView[@content-desc="Image"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.add_button = self.driver.find_element(By.ID, value=self.ADD_BUTTON)
        self.schedule_for_today = self.driver.find_element(By.ID, value=self.TODAY_SCHEDULE)
        self.tomorrow = self.driver.find_element(By.XPATH, value=self.TOMORROW_BUTTON)
        self.next_week = self.driver.find_element(By.XPATH, value=self.NEXT_WEEK)

    def click_on_add_button(self):
        self.add_button.click()
        return self.add_button

    def click_on_tomorrow_add_event(self):
        self.click_on_add_button()
        time.sleep(3)
        self.tomorrow.click()
        return self.tomorrow

    def click_on_today_schedule(self):
        self.schedule_for_today.click()
        return self.schedule_for_today

    def click_on_nex_week_button(self):
        self.next_week.click()
        return self.next_week


