import requests
import uuid
from config import get_value_from_api

def translate_text(text, lang,city):
    key =get_value_from_api('TRANSLATOR_KEY')
    endpoint = get_value_from_api('TRANSLATOR_ENDPOINT')
    
    location = "eastus"
    path = '/translate'
    constructed_url = endpoint + path
    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': str(lang)
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': f'The weather forecast for {city} is {text["weather"][0]["description"]} with a temperature of {text["main"]["temp"]} degree celsius and a humidity of {text["main"]["humidity"]} percent and a wind speed of {text["wind"]["speed"]} meter per second.'
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    print('Translated weather report:', response[0]['translations'][0]['text'])
