from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class YouTubeShortPage(BasePage):
    SHORT_PAGE = "//ytd-mini-guide-entry-renderer[2]/a[@id='endpoint']"

    def __init__(self, driver):
        super().__init__(driver)
        self.shorts_button = self._driver.find_element(By.XPATH, self.SHORT_PAGE)

    def click_on_the_short_video_page_on_youtube(self):
        self.shorts_button.click()

