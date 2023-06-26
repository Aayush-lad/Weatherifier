import click
import geocoder
import pyperclip
import matplotlib.pyplot as plt
from art import tprint
from weather import get_weather, print_weather_data
from forecast import get_forecast,  generate_weather_report, visualize_weather_report, plot_forecast
from audio import text_to_speech
from sentiment import analyze_sentiment
from translation import translate_text


@click.command()
@click.option('--city', '-c', help='Display weather for a specific city.')
@click.option('--forecast', '-f', is_flag=True, help='Display 5-day weather forecast and plot the graph.')
@click.option('--geolocation', '-g', is_flag=True, help='Get weather based on geolocation.')
@click.option('--share', '-s', is_flag=True, help='Share the weather report.')
@click.option('--tts', '-t', is_flag=True, help='Convert weather report to audio.')
@click.option('--comment', '-cm', help='Analyze sentiment of a weather-related comment.')
@click.option('--translate', '-tr', help='Translate weather description to a specific language.')
def weather(city, forecast, geolocation, share, tts, comment, translate):
    tprint("Welcome to Weatherifier!!", font="small")
    print("How to use: run the command python weatherifier.py -c <city name> /-f /-s /-t /-cm <comment> /-g")
    print("For help, run the command python weatherifier.py --help")
    click.echo()

    if geolocation:
        g = geocoder.ip('me')
        city = g.city

    if city:
        try:
            weather_data = get_weather(city)
            click.echo(f"Weather forecast for {city}:")
            click.echo()
            print_weather_data(weather_data)
        except Exception as err:
            print("City was not found in database . pls try another nearby city")


    if translate:
        description = get_weather(city)
        try:
            translated_text = translate_text(description, translate,city)
        except Exception as err:
            click.echo(err);

    if forecast:
        forecast_data = get_forecast(city)
        click.echo(f"Weather forecast for the next 5 days in {city}:")
        click.echo()
        for data in forecast_data['list']:
            click.echo(data['dt_txt'])
            weather_report = generate_weather_report(data)
            visualize_weather_report(weather_report)
            click.echo()
        plot_forecast(forecast_data)

        if share:
            weather_report = generate_weather_report(weather_data)
            pyperclip.copy(weather_report)
            click.echo("Weather report copied to clipboard. You can now paste it anywhere.")

    if tts:
        weather_data = get_weather(city)

        weather_report = 'The weather forecast for ' + city + ' is ' + weather_data['weather'][0]['description'] + ' with a temperature of ' + str(weather_data['main']['temp']) + ' degree Celsius, a humidity of ' + str(weather_data['main']['humidity']) + ' percent, and a wind speed of ' + str(weather_data['wind']['speed']) + ' meters per second. Thank you.'

        # Generate a unique audio file name
        audio_file = f'{city}_weather_report.wav'

        try:
            text_to_speech(weather_report, audio_file)
            click.echo('Weather report audio generated successfully.')

        except Exception as e:
            click.echo(f'Error generating audio: {str(e)}')

    if comment:
        analyze_sentiment(comment)


if __name__ == '__main__':
    weather()
