from flask import Blueprint, render_template, request, redirect
from .flights import FlightsData, SingleFlight
from .models import User
from .authentication.auth import UserClass
from flask_login import login_required, current_user
from .wikipediaAPI.wikipedia import WikipediaData
from .coinCurrencyAPI.currencyCodes import CurrencyISOcode
from .coinCurrencyAPI.currency import CurrencyData
from .covidAPI.covid import Covid
from .weatherAPI.weather import Weather


# Main file 


main = Blueprint('main', __name__)


# API i used - flight, wiki, currency, get ISO name, covid19, weather .


@main.route('/')
def index():
    """
    Home page with flights table
    """
    flights = FlightsData().viewAll()
    return render_template('index.html', flights=flights)



@main.route('/register', methods=['GET', 'POST'])
def register():
    """
    Register page
    """
    message = ''
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        pass1 = request.form.get('pass1')
        pass2 = request.form.get('pass2')
        
        # Tests before I insert into the DB

        if pass1 != pass2:
            message = 'Password not mach'
            return render_template('regiset.html', message=message)
        user = User.query.filter_by(email=email).first()

        if user:
            message = 'Email alaredy exist'
            return render_template('regiset.html', message=message)
        
        else:
            UserClass().sign_up(fname, lname, email, pass1)
            return redirect('/login')
    return render_template('register.html')



@main.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login Page
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        sing_in = UserClass().sign_in(email, password)

        if sing_in is not None:
            return redirect('/')
    return render_template('login.html')



@main.route('/logout')
@login_required
def logout():
    """
    Logout function
    """
    UserClass().sign_out()
    return redirect('/')



@main.route('/flight/<num>', methods=['GET', 'POST'])
def flight(num):
    """
    Single Flight detail page
    """
    flight_detail = FlightsData().viewOne(num)
    wiki = WikipediaData(flight_detail.country).all()
    currency = CurrencyData(CurrencyISOcode(flight_detail.country).currency()).convertcoin()
    coronavirus = Covid(flight_detail.country).get()
    weather = Weather(flight_detail.country).main()
    return render_template('flight_single.html', flight_detail=flight_detail, wiki=wiki, currency=currency, coronavirus=coronavirus, weather=weather)



@main.route('/flight/country/<countryName>', methods=['GET', 'POST'])
def country_detail(countryName):
    """
    Couple details on the country
    """
    wiki = WikipediaData(countryName).all()
    flag = CurrencyISOcode(countryName).flag()
    weather = Weather(countryName).main()
    return render_template('country_detail.html', wiki=wiki, flag=flag, weather=weather, name=countryName)



@main.route('/flight/search')
def search():
    """
    Search function
    """
    q = request.args.get('q')
    flight_detail = FlightsData().viewOne(q)
    wiki = WikipediaData(flight_detail.country).all()
    currency = CurrencyData(CurrencyISOcode(flight_detail.country).currency()).convertcoin()
    coronavirus = Covid(flight_detail.country).get()
    weather = Weather(flight_detail.country).main()
    return render_template('search.html', flight_detail=flight_detail, wiki=wiki, currency=currency, coronavirus=coronavirus, weather=weather)

    

@main.route('/flights/your-flights')
def your_flights():
    """
    Client save flights
    """
    flights = SingleFlight(current_user.id).view()
    return render_template('yourFlights.html', flights=flights)



@main.route('/save/')
@login_required
def save_flights():
    """
    Save flights function
    """
    id = request.args.get('id')
    SingleFlight(current_user.id).save(id) # Save
    return redirect('/flights/your-flights')

    

@main.route('/save/remove', methods=['GET', 'POST'])
@login_required
def removeFlight():
    """
    Remove single flight from save flights
    """
    if request.method == 'POST':
        num = request.form.get('num')
        SingleFlight(current_user.id).remove(num)
        return redirect('/flights/your-flights')


