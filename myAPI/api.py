from flask import Blueprint, request
from flask_restful import Resource, Api
from flask_cors import CORS
from .key import Key
from ..flights import FlightsData
from ..wikipediaAPI.wikipedia import WikipediaData
from ..coinCurrencyAPI.currency import CurrencyData
from ..coinCurrencyAPI.currencyCodes import CurrencyISOcode
from ..covidAPI.covid import Covid
from ..weatherAPI.weather import Weather
from ..authentication.auth import UserClass


# My own API 


api = Blueprint('api',__name__)


CORS(api)
api_app = Api(api)


class GenereteKey(Resource):

    def post(self): # To use the API you need to be a user 
        data = request.get_json()
        check = UserClass().check(data['email'], data['password'])
        if check is not None:
            key = Key().create()
            return key, 201
        else:
            return {'Message': 'email or password incorrect'}, 404



class FlightsAll(Resource):

    def get(self):
        key = request.args.get('key')
        check = Key().check(key)
        if check is not None:
            return FlightsData().viewAll(), 201    
        else:
            return Key().key_error(), 400



class FlightOne(Resource):

    def get(self):
        key = request.args.get('key')
        flight = request.args.get('flight')
        check = Key().check(key)
        if check is not None:
            data = FlightsData().viewOne(flight).serialize()
            wiki = WikipediaData(data['country']).all()
            currency = CurrencyData(CurrencyISOcode(data['country']).currency()).convertcoin()
            coronavirus = Covid(data['country']).get()
            weather = Weather(data['country']).main()
            return {
                'flight': data,
                'wiki':wiki,
                'currency': currency,
                'covid': coronavirus,
                'weather': weather
            }, 201
        else:
            return Key().key_error(), 400



# My Api key - cc17a13f95e4c375f456ebe691bfa076

# For get API key - http://127.0.0.1:5000/api/flights/key/ - Method -> POST
api_app.add_resource(GenereteKey,'/api/flights/key/')

# For get all flights - http://127.0.0.1:5000/api/flights/all?{Your Api Key} - Method -> Get
api_app.add_resource(FlightsAll, '/api/flights/all')

# For get detail about single flight - http://127.0.0.1:5000/api/flights/all?{Your Api Key}&flight={Flight Number}
api_app.add_resource(FlightOne, '/api/flights/one')


