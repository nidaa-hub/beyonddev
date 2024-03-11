import unittest

import requests

from infra.api_wrapper import APIWrapper
from logic.deck_of_cards import DeckOfCards


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.api_logic = DeckOfCards(self.my_api)

    def test_the_status(self):
        response = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
        assert response.status_code == 200, f'Expected status code 200, but got{response.status_code}'

    def test_deck_id(self):
        result = self.api_logic.shuffle_the_cards_id()
        assert result, "tmnr8afvl6bf"

    def test_check_the_image_of_all_the_cards(self):
        result = self.api_logic.get_image_of_the_card()
        assert result, f"Failed to open the link: {'https://deckofcardsapi.com/static/img/KS.png'}"

    def test_brand_new_deck(self):
        result = self.api_logic.brand_new_deck_json()
        assert result, 52

    def test_check_back_of_the_cards(self):
        result = self.api_logic.back_of_card_image()
        assert result, f"Failed to open the link: {'https://deckofcardsapi.com/static/img/back.png'}"
