import urllib.request
import json
from .models import Flights, FlightSave
from . import db


# Flight API


class FlightsData:
    url = "https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&limit=20"

    def __init__(self):
        self._initialize()


    def data(self):
        fileobj = urllib.request.urlopen(self.url)
        read = fileobj.read().decode()
        load = json.loads(read)
        rows = load['result']['records']
        return self.save(rows)


    def _initialize(self): # ? _initialize
        self.data()
        

    def save(self, rows):
        flights = Flights.query.delete(), FlightSave.query.delete() # Delete data to get new data and dont save data that i dont need, and save always on 20 flights data
        for row in rows:
            if row['CHRMINE'] == 'LANDED':
                flight_num = row['CHOPER'] + row['CHFLTN']
                airline = row['CHOPERD'].lower()
                city = row['CHLOC1D'].lower()
                country = row['CHLOCCT'].lower()
                status = row['CHRMINE']
                official_time = row['CHSTOL']
                real_time = row['CHPTOL']
                bool = True
                flights = Flights(flight_num=flight_num,airline=airline,city=city,country=country,status=status,official_time=official_time,real_time=real_time,to=bool)
                db.session.add(flights)
                db.session.commit()
            else:
                flight_num = row['CHOPER'] + row['CHFLTN']
                airline = row['CHOPERD'].lower()
                city = row['CHLOC1D'].lower()
                country = row['CHLOCCT'].lower()
                status = row['CHRMINE']
                official_time = row['CHSTOL']
                real_time = row['CHPTOL']
                bool = False
                flights = Flights(flight_num=flight_num,airline=airline,city=city,country=country,status=status,official_time=official_time,real_time=real_time,to=bool)
                db.session.add(flights)
                db.session.commit()               
        

    def viewAll(self):
        self._initialize()
        flights = Flights.query.all()
        return [flight.serialize() for flight in flights]

    
    def viewOne(self, flightNum):
        flight = Flights.query.filter_by(flight_num=flightNum).first()
        return flight




class SingleFlight:

    def __init__(self, userId):
        self.user = userId


    def save(self, flightId):
        save = FlightSave(user=self.user,flight=flightId)
        db.session.add(save)
        db.session.commit()

    
    def view(self):
        flights = FlightSave.query.filter_by(user=self.user).all()
        return flights


    def remove(self, flightNum):
        FlightSave.query.filter_by(
            user=self.user,flight=flightNum).delete()
        db.session.commit()
        

