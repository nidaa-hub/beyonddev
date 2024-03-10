import unittest

import requests

from infra.api_wrapper import APIWrapper
from logic.planetary_apod import Planetary_Apod


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.api_logic = Planetary_Apod(self.my_api)

    def test_check_status_code_in_Astronomy_Picture_of_the_Day(self):
        result = self.api_logic.planetary_apod_api()
        self.assertTrue(result.ok)

    def test_check_the_image_in_the_Astronomy_Picture_of_the_Day(self):
        result = self.api_logic.get_image_of_the_day_url()
        assert result, f"Failed to open the link: {'https://apod.nasa.gov/apod/image/2403/2024_03_05_Pons-Brooks_Revuca_1200px.png'}"

    def test_check_the_image_of_the_earth(self):
        result = self.api_logic.get_image_of_the_earth()
        assert result, f"Failed to open the link: {'https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png?api_key=d08C9CyffXKrI9MiwdLE8N3tDi0hnkEHVUgJCa4S'}"

  #  def test_check_the_image_of_the_earth(self):
   #     result = self.api_logic.planetary_satalet_api()

    def test_the_status(self):
        response = requests.get('http://tle.ivanstanojevic.me/api/tle/25544')
        assert response.status_code == 200, f'Expected status code 200, but got{response.status_code}'