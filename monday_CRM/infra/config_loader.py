import json

from os.path import dirname, join


class ConfigLoader:
    def get_filename(self, filename):
        here = dirname(__file__)
        output = join(here, filename)
        return output

    def load_config(self, file_path="../config.json"):  #
        filename = self.get_filename(file_path)
        with open(filename, 'r') as file:
            config = json.load(file)
        return config
