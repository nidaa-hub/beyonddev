from infra.base_page import BasePage
from selenium.webdriver.common.by import By

class YouTubeTrendingPage(BasePage):
    MENU = "guide-icon"
    TRENDING_PAGE = "//ytd-guide-section-renderer[3]/div/ytd-guide-entry-renderer[1]"

    def __init__(self, driver):
        super().__init__(driver)
        self.menu_button = self._driver.find_element(By.ID, self.MENU)
        self.trending_button = self._driver.find_element(By.XPATH, self.TRENDING_PAGE)

    def click_on_the_menu_on_youtube(self):
        self.menu_button.click()

    def click_on_the_trending_video_page_on_youtube(self):
        self.trending_button.click()

    def open_trending_page(self):
        self.click_on_the_menu_on_youtube()
        self.click_on_the_trending_video_page_on_youtube()

