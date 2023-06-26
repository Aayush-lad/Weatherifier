import requests
import click
import matplotlib.pyplot as plt
from colorama import Fore, Style
from config import get_value_from_api
API_KEY = get_value_from_api('API_KEY')
FORECAST_URL = 'http://api.openweathermap.org/data/2.5/forecast'

WEATHER_SYMBOLS = {
    'Clear': '☀️',
    'Clouds': '☁️',
    'Rain': '🌧️',
    'Drizzle': '🌦️',
    'Thunderstorm': '⛈️',
    'Snow': '❄️',
    'Mist': '🌫️',
    'Haze': '🌫️'
}
def get_forecast(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(FORECAST_URL, params=params)
    forecast_data = response.json()
    return forecast_data


def print_forecast_data(data):
    for forecast in data['list']:
        date = forecast['dt_txt']
        temperature = forecast['main']['temp']
        weather = forecast['weather'][0]['main']
        weather_symbol = WEATHER_SYMBOLS.get(weather, '')

        click.echo(f"{date}")
        click.echo(f"Temperature: {temperature}°C")
        click.echo(f"Weather: {weather_symbol} {weather}")
        click.echo()


def generate_weather_report(data):
    report = ''
    report += f"Temperature: {data['main']['temp']}°C\n"
    report += f"Weather: {data['weather'][0]['main']}\n"
    report += f"Description: {data['weather'][0]['description']}\n"
    report += f"Humidity: {data['main']['humidity']}%\n"
    report += f"Wind Speed: {data['wind']['speed']} m/s\n"
    return report


def visualize_weather_report(weather_report):
    lines = weather_report.split('\n')
    for line in lines:
        if line.startswith('Weather:'):
            weather = line.split(': ')[1]
            weather_symbol = WEATHER_SYMBOLS.get(weather, '')
            line = f"{Fore.YELLOW}{line} {weather_symbol}{Style.RESET_ALL}"
        click.echo(line)


def plot_forecast(forecast_data):
    dates = []
    temperatures = []
    for data in forecast_data['list']:
        date = data['dt_txt']
        temperature = data['main']['temp']
        dates.append(date)
        temperatures.append(temperature)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperatures, marker='o', linestyle='-', color='b')
    plt.title('Weather Forecast')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()
