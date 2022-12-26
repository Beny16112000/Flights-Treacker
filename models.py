from . import db
from flask_login import UserMixin


# db Models


class Flights(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_num = db.Column(db.String(200), nullable=False)
    airline = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200), nullable=False)
    official_time = db.Column(db.String(200), nullable=False)
    real_time = db.Column(db.String(200), nullable=False)
    to = db.Column(db.Boolean, default=False)

    def serialize(self):
        return {
            'id': self.id,
            'flight_num': self.flight_num ,
            'airline': self.airline ,
            'city': self.city ,
            'country': self.country ,
            'status': self.status ,
            'official_time': self.official_time ,
            'real_time': self.real_time ,
            'to': self.to ,
        }



class User(UserMixin ,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(1000),nullable=False)
    last_name = db.Column(db.String(1000),nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100),nullable=False)



class FlightSave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    flight = db.Column(db.String(200), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'user': self.user,
            'flight': self.flight
        }



class Keys(db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True)

    def serialize(self):
        return {
            'id': self.id,
            'key': self.key
        }


