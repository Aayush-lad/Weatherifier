import requests
import click

from config import get_value_from_api
API_KEY = get_value_from_api('API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    weather_data = response.json()
    return weather_data


def print_weather_data(data):
    click.echo(f"Temperature: {data['main']['temp']}°C")
    click.echo(f"Weather: {data['weather'][0]['main']}")
    click.echo(f"Description: {data['weather'][0]['description']}")
    click.echo(f"Humidity: {data['main']['humidity']}%")
    click.echo(f"Wind Speed: {data['wind']['speed']} m/s")
    click.echo()
