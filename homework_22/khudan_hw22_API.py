import requests
import json

class BreakingBadAPI:
    def __init__(self, base_url='https://swapi.dev/api/people/5'):
        self.base_url = base_url

    def get_characters(self):
        url = f"{self.base_url}"
        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()
            self.save_json_to_file(json_data, 'character.json')
        else:
            print(f"Error: {response.status_code}")

    def save_json_to_file(self, json_data, filename):
        with open(filename, 'w') as file:
            json.dump(json_data, file)

# Приклад використання класу
api = BreakingBadAPI()
api.get_characters()
