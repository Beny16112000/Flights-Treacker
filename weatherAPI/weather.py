import requests


# Wether data API, APIkey = 2bb2d3c262e87a1c26cc267885212179 


class Weather:

    def __init__(self, location):
        self.location = location


    def open(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.location}&appid=2bb2d3c262e87a1c26cc267885212179&units=metric"
        response = requests.get(url)
        data = response.json()
        return data


    def all(self):
        data = self.open()
        return data   

     
    def main(self):
        data = self.open()
        return data['main']


