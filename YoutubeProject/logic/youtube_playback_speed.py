from infra.base_page import BasePage
from selenium.webdriver.common.by import By

class YouTubePlayBackSpeed(BasePage):

    FIRST_VIDEO_PLAY = "//ytd-app//ytd-page-manager//ytd-rich-grid-row[2]//ytd-thumbnail"
    PLAYBACKSPEEDSETTING = "//ytd-watch-flexy//div[2]/button[4]"
    PLAYBACKSPEED = "//div[@id='ytp-id-18']/div/div/div[3]"

    def __init__(self, driver):
        super().__init__(driver)
        self.video_play = self._driver.find_element(By.XPATH, self.FIRST_VIDEO_PLAY)
        self.playback_speed_setting = self._driver.find_element(By.XPATH, self.PLAYBACKSPEEDSETTING)
        self.playback_speed_button = self._driver.find_element(By.XPATH, self.PLAYBACKSPEED)

    def click_on_the_first_video(self):
        self.video_play.click()

    def click_on_setting_button_on_video_on_youtube(self):
        self.playback_speed_setting.click()

    def click_on_playback_speed_button_on_youtube(self):
        self.playback_speed_button.click()
