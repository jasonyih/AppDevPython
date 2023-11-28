import requests
import json

class Cat:

    def __init__(self):
        self.url = 'https://catfact.ninja/breeds'

    def nth_breed(self, n):
        result = requests.get(self.url)
        data = result.json()
        data = data['data'][n]
        format = json.dumps(data, indent=2)
        print(format)


catfact = Cat()
catfact.nth_breed(2)
