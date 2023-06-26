import requests

def get_value_from_api(key):
    url = 'https://keyvault.onrender.com/api/get-value'
    params = {'key': key}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['value']
    elif response.status_code == 400:
        print('Error: Key is required')
    elif response.status_code == 404:
        print('Error: Key not found')
    else:
        print('Error: Failed to retrieve data')

