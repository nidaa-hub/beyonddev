import unittest
from logic.home_page import Calender
from infra.browser_wrapper import BrowserWrapper
from logic.menu import MenuPage


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = BrowserWrapper()
        self.driver = self.driver.get_driver()

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_add_event_button(self):
        self.calender = Calender(self.driver)
        self.add_button = self.calender.click_on_add_button()
        assert self.add_button.is_displayed(), "Button is not displayed"

    def test_view_event_in_specific_day_on_calender(self):
        self.calender = Calender(self.driver)
        self.add_event_today = self.calender.click_on_today_schedule()
        assert self.add_event_today.is_displayed(), "Button is not displayed"

    def test_add_event_on_tomorrow_schedule(self):
        self.calender = Calender(self.driver)
        self.add_event = self.calender.click_on_tomorrow_add_event()
        assert self.add_event.is_displayed(), "Button is not displayed"

    def test_dark_mode_on(self):
        self.menu = MenuPage(self.driver)
        self.menu_button = self.menu.dark_mode_app()
        assert self.menu_button.is_displayed(), "Button is not displayed"

    def test_next_week_calender(self):
        self.calender = Calender(self.driver)
        self.next_button = self.calender.click_on_nex_week_button()
        assert self.next_button.is_displayed(), "Button is not displayed"


