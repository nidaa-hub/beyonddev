import webbrowser

from infra.api_wrapper import APIWrapper
import json

class Planetary_Apod:

    apiKey = 'd08C9CyffXKrI9MiwdLE8N3tDi0hnkEHVUgJCa4S'

    def __init__(self, api_object):
        self.my_api = api_object
        self.my_api = APIWrapper()

    def planetary_apod_api(self):
        result = self.my_api.api_get_request(f'https://api.nasa.gov/planetary/apod?api_key={self.apiKey}')
        return result.json()

    def get_image_of_the_day_url(self):
        image = self.planetary_apod_api()
        image_url = image["url"]
        webbrowser.open(image_url)
        return image_url

    def get_image_of_the_earth(self):
        earth_image = f'https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png?api_key={self.apiKey}'
        webbrowser.open(earth_image)
        return earth_image

    def planetary_satellite_api(self):
        result = self.my_api.api_get_request(f'http://tle.ivanstanojevic.me/api/tle/25544')
        print(result)
        return result
