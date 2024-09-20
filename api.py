# from flask import Flask,render_template
# import requests
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# @app.route('/')
# def index():
#     url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=25d3252148432ed7a153fa0bb2e2ab47'
#     city = 'Hyderabad'
#     r = requests.get(url.format(city)).json()

#     weather = {
#         'city' : city,
#         'temperature': r['main']['temp'],
#         'description': r['weather'][0]['description'],
#         'icon':r['weather'][0]['icon']
#     }



#     return render_template('weather.html',weather=weather)


# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Store cities in a list instead of a database
cities = ['New York', 'London', 'Tokyo']

def get_weather_data(city):
    api_key = '25d3252148432ed7a153fa0bb2e2ab47'  # Replace with your actual API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=25d3252148432ed7a153fa0bb2e2ab47'
    try:
        response = requests.get(url)
        data = response.json()
        return {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
    except:
        return None

@app.route('/')
def index():
    weather_data = []
    for city in cities:
        data = get_weather_data(city)
        if data:
            weather_data.append(data)
    return render_template('weather.html', weather_data=weather_data)

@app.route('/add', methods=['POST'])
def add_city():
    new_city = request.form.get('city')
    if new_city and new_city not in cities:
        cities.append(new_city)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)