import json
import csv

class JsonToCsvAdapter:
    def __init__(self, json_file):
        with open(json_file) as f:
            self.data = json.load(f)

    def to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # записуємо заголовки з ключів json
            writer.writerow(self.data[0].keys())

            # записуємо рядки зі значеннями
            for item in self.data:
                writer.writerow(item.values())

adapter = JsonToCsvAdapter('example.json')
adapter.to_csv('output.csv')
