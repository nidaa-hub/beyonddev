import time
import unittest

from selenium.webdriver.common.by import By
from infra.browser_wrapper import BrowserWrapper
from logic.youtube_page import YouTubePage
from logic.youtube_short_page import YouTubeShortPage
from logic.youtube_trending_page import YouTubeTrendingPage
from logic.youtube_full_screen_mode import YouTubeFullScreen
from logic.youtube_playback_speed import YouTubePlayBackSpeed


class Youtube_Page_Test(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://www.youtube.com")

    def tearDown(self):
        self.driver.quit()

    def test_check_title_for_search(self):
        self.youtube_page = YouTubePage(self.driver)
        self.youtube_page.search_flow("Python programming")
        self.youtube_page.choose_the_first_veido_on_the_list(self.driver)
        time.sleep(10)
        self.assertIn("Python programming", self.youtube_page.get_page_title(), "the title not show")

    def test_shorts_page_on_youtube(self):
        self.youtube_short_page = YouTubeShortPage(self.driver)
        self.youtube_short_page.click_on_the_short_video_page_on_youtube()
        time.sleep(10)
        print("Shorts Page YouTube")

    def test_video_playback_speed(self):
        self.youtube_full_screen_video = YouTubeFullScreen(self.driver)
        self.youtube_full_screen_video.click_on_the_first_video_on_youtube()
        time.sleep(3)
        self.youtube_playback_speed = YouTubePlayBackSpeed(self.driver)
        self.youtube_playback_speed.click_on_setting_button_on_video_on_youtube()
        self.youtube_playback_speed.click_on_playback_speed_button_on_youtube()
        time.sleep(5)
        print("video playback speed")

    def test_play_full_screen_video_on_youtube(self):
        self.youtube_full_screen_video = YouTubeFullScreen(self.driver)
        self.youtube_full_screen_video.click_on_the_first_video_on_youtube()
        time.sleep(3)
        self.youtube_full_screen_video.click_on_full_screen_mode_on_youtube()
        time.sleep(5)
        print("Full screen on YouTube")

    def test_stop_video_on_youtube(self):
        self.play = self.driver.find_element(By.XPATH, "//ytd-app//ytd-page-manager//ytd-rich-grid-row[2]//ytd-thumbnail")
        self.play.click()
        time.sleep(10)
        self.stop = self.driver.find_element(By.XPATH, "//div[@id='movie_player']/div[35]/div[2]/div[1]/button[@class='ytp-play-button ytp-button']")
        self.stop.click()
        time.sleep(10)

    def test_trending_video_on_youtube(self):
        self.youtube_trending_page = YouTubeTrendingPage(self.driver)
        self.menu_button = self.driver.find_element(By.ID, "guide-icon")
        self.menu_button.click()
        self.trending_button = self.driver.find_element(By.XPATH, "//ytd-guide-section-renderer[3]/div/ytd-guide-entry-renderer[1]")
        self.trending_button.click()
        time.sleep(10)
        print("Trending Page YouTube")








