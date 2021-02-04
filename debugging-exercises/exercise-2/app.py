import os
import requests

from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file, redirect


################################################
## SETUP
################################################

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('API_KEY')


################################################
## ROUTES
################################################

@app.route('/')
def home():
    """Displays the homepage with forms for current or historical data."""
    context = {
        'min_date': (datetime.now() - timedelta(days=5)),
        'max_date': datetime.now(),
        'err': request.args.get('err')
    }
    return render_template('home.html', **context)

def get_letter_for_units(units):
    """Returns a shorthand letter for the given units."""
    return 'F' if units == 'imperial' else 'C' if units == 'metric' else 'K'

@app.route('/results')
def results():
    """Displays results for current weather conditions."""
    city = request.args.get('city')
    units = request.args.get('requested_units')

    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'units': units,
        'appid': API_KEY,
    }
    result_json = requests.get(url, params=params).json()
    if result_json['cod'] == '400':
        return redirect("/?err=Invalid city.")
    context = {
        'date': datetime.now(),
        'city': result_json['name'],
        'description': result_json['weather'][0]['description'],
        'temp': result_json['main']['temp'],
        'humidity': result_json['main']['humidity'],
        'wind_speed': result_json['wind']['speed'],
        'units_letter': get_letter_for_units(units)
    }

    return render_template('results.html', **context)


if __name__ == '__main__':
    app.run()