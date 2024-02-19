from infra.base_page import BasePage
from selenium.webdriver.common.by import By

class YouTubeStopVideo(BasePage):

    FIRST_VIDEO_PLAY = "//ytd-app//ytd-page-manager//ytd-rich-grid-row[2]//ytd-thumbnail"
    STOPBUTTON = "//ytd-player[@id='inline-preview-player']/div[19]/div[1]"

    def __init__(self, driver):
        super().__init__(driver)
        self.video_play = self._driver.find_element(By.XPATH, self.FIRST_VIDEO_PLAY)
        self.played_video = self._driver.find_element(By.XPATH, self.STOPBUTTON)

    def click_on_the_first_video(self):
        self.video_play.click()

    def stop_video(self):
        self.played_video.click()