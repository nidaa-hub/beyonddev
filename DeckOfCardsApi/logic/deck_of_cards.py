import webbrowser
from infra.api_wrapper import APIWrapper

class DeckOfCards:

    def __init__(self, api_object):
        self.my_api = api_object
        self.my_api = APIWrapper()

    def shuffle_the_cards_id(self):
        result = self.my_api.api_get_request(f'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
        response_json = result.json()
        deck_id = response_json["deck_id"]
        return deck_id

    def draw_a_card_json(self):
        response = self.my_api.api_get_request(f'https://deckofcardsapi.com/api/deck/tmnr8afvl6bf/draw/?count=2')
        return response.json()

    def get_image_of_the_card(self):
        response_json = self.draw_a_card_json()
        for card in response_json["cards"]:
            image_url = card["image"]
            webbrowser.open(image_url)
        print(image_url)
        return image_url

    def brand_new_deck_json(self):
        response = self.my_api.api_get_request(f'https://deckofcardsapi.com/api/deck/new/')
        response_json = response.json()
        remaining = response_json["remaining"]
        return remaining

    def back_of_card_image(self):
        image = "https://deckofcardsapi.com/static/img/back.png"
        webbrowser.open(image)
        return image

