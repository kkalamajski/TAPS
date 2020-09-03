import requests

def exchange_rate():
    try:
        query = {'base':'USD','symbols':'PLN'}
        r = requests.get('https://api.exchangeratesapi.io/latest', params=query)
        print(r.text)
    except TimeoutError:
        print('Timeout')

exchange_rate()