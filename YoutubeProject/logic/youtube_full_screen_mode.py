from infra.base_page import BasePage
from selenium.webdriver.common.by import By

class YouTubeFullScreen(BasePage):

    FIRST_VIDEO_PLAY = "//ytd-app//ytd-page-manager//ytd-rich-grid-row[2]//ytd-thumbnail"
    FULL_SCREEN = "//button[9]"

    def __init__(self, driver):
        super().__init__(driver)
        self.video_play_button = self._driver.find_element(By.XPATH, self.FIRST_VIDEO_PLAY)

    def click_on_the_first_video_on_youtube(self):
        self.video_play_button.click()

    def click_on_full_screen_mode_on_youtube(self):
        self.full_screen_button = self._driver.find_element(By.XPATH, self.FULL_SCREEN)
        self.full_screen_button.click()