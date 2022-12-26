from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


# Set app


db = SQLAlchemy()


def create_app():
    """
    Config & create app
    """
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'fvdfvfdmjmkmklwfwef'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights.sqlite'

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .myAPI.api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    # register models 
    
    from .models import Flights, User, FlightSave, Keys

    create_database(app)

    # Authentication setup

    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    return app


def create_database(app):
    """
    Creating db
    """
    if not path.exists('flights-tracker/' + 'flights.db'):
        db.create_all(app=app)
        print('Created Database !')
