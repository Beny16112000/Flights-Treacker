import urllib.request
import json
from urllib.error import HTTPError


# Find ISO code by country


class CurrencyISOcode:
    
    def __init__(self, name):
        self.name = name


    def file(self):
        try:
            url = f"https://restcountries.com/v3.1/name/{self.name}?fullText=true"
            fileobj = urllib.request.urlopen(url)  
            read = fileobj.read().decode()
            data = json.loads(read)
            return data
        except HTTPError:
            None


    def currency(self):
        file = self.file()
        if file is not None:
            data = file[0]['currencies']
            data = data.keys()
            data = list(data)
            return data[0]
        else:
            return None


    def flag(self):
        file = self.file()
        if file is not None:
            flag = file[0]['coatOfArms']['png']
            return flag


