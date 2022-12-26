import requests
from datetime import date, timedelta
import json


# Covid19 API


class Covid:
    def __init__(self, country):
        self.country = country


    def get(self):
        url = f'https://api.api-ninjas.com/v1/covid19?country={self.country}'
        response = requests.get(url, headers={'X-Api-Key': 'GuiUnnP5cKdEmH64Kkd6Kg==eCtInxo6VydFsWjT'})
        if response.status_code == requests.codes.ok:
            today = date.today()
            yesterday = today - timedelta(days = 2)
            yesterday = str(yesterday)
            data = json.loads(response.text)[0]['cases'][yesterday]
            return data

        else:
            return "Error", response.status_code, response.text

