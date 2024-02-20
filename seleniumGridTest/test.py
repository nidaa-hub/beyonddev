import time
import unittest
import concurrent.futures
from selenium import webdriver
from logic.logic_page import LogicPage
from infra.browser_wrapper import BrowserWrapper


class GridTest(unittest.TestCase):
    HUB_URL = 'http://172.20.10.3:4444'

    def setUp(self):
        self.chrome_cap = webdriver.ChromeOptions()
        self.chrome_cap.capabilities['platformName'] = 'windows'

        self.edge_cap = webdriver.EdgeOptions()
        self.edge_cap.capabilities['platformName'] = 'windows'

        self.cap_list = [self.chrome_cap, self.edge_cap]
        self.browser = BrowserWrapper()

    def test_run_grid_serial(self):
        for cap in self.cap_list:
            self.test_execute(cap)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_execute, self.cap_list)

    def test_execute(self, cap):
        self.driver = self.browser.get_driver(cap)
        self.logic = LogicPage(self.browser.get_driver(cap))

        print("test run on: ", cap.capabilities)

        self.assertEqual(" ", self.logic.execute(), "Title doesn't match expected value")
        time.sleep(2)
        self.driver.quit()

    def test_run_grid_serial_instagram_icon(self):
        for cap in self.cap_list:
            self.test_the_instagram_icon_can_click(cap)

    def test_run_grid_parallel_instagram_icon(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_the_instagram_icon_can_click, self.cap_list)

    def test_the_instagram_icon_can_click(self):
        self.instagram_icon = LogicPage(self.driver)
        self.instagram_icon.click_on_instagram_button()
        time.sleep(10)
        button = self.instagram_icon.instagram_button_to_check
        assert button.is_displayed()
        print("Instagram icon work")

    def test_run_grid_serial_my_score(self):
        for cap in self.cap_list:
            self.test_the_my_score_can_click(cap)

    def test_run_grid_parallel_my_score(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_the_my_score_can_click, self.cap_list)

    def test_the_my_score_can_click(self):
        self.my_score = LogicPage(self.driver)
        self.my_score.click_on_my_score_button()
        time.sleep(10)
        button = self.my_score.click_on_my_score_button()
        assert button.is_displayed()
        print("my score is working")

    def test_run_grid_search(self):
        for cap in self.cap_list:
            self.test_check_title_for_search(cap)

    def test_run_grid_parallel_search(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_check_title_for_search, self.cap_list)

    def test_check_title_for_search(self):
        self.search_input = LogicPage(self.driver)
        self.search_input.search_flow("barcelona")
        time.sleep(10)
        self.assertIn("barcelona", self.search_input.get_page_title(), "the title not show")

    def test_run_grid_serial_home_page_icon(self):
        for cap in self.cap_list:
            self.test_back_to_home_page_icon(cap)

    def test_run_grid_parallel_home_page_icon(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_back_to_home_page_icon, self.cap_list)

    def test_back_to_home_page_icon(self):
        self.home_page_icon = LogicPage(self.driver)
        self.home_page_icon.click_on_page_icon_button()
        time.sleep(10)
        button = self.page_icon_button_to_check
        assert button.is_displayed()
        print("Back to home page through the icon")

    def test_run_grid_serial_advertising_page(self):
        for cap in self.cap_list:
            self.test_advertising_page(cap)

    def test_run_grid_parallel_advertising_page(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_advertising_page, self.cap_list)

    def test_advertising_page(self):
        self.advertising = LogicPage(self.driver)
        self.advertising.click_on_advertising_page()
        time.sleep(10)
        button = self.page_advertising_button_to_check()
        assert button.is_displayed()
        print("The advertising button work")
