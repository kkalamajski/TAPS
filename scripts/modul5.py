import requests
import json
import time

def stats(function):
    def wrapper():
            while True:
                function()
                query = {'base': 'USD', 'symbols': 'PLN'}
                r = requests.get('https://api.exchangeratesapi.io/latest', params=query)
                print('Data i godzina wysłania zapytania:', r.headers['Date'])
                print('Czas wykonania zapytania: ', r.elapsed.total_seconds(), 's')
                time.sleep(15)
    return wrapper()

@stats
def exchange_rate():
    try:
        query = {'base': 'USD', 'symbols': 'PLN'}
        r = requests.get('https://api.exchangeratesapi.io/latest', params=query)
        response_dictionary = json.loads(r.content)
        rates = response_dictionary['rates']
        print('Kurs', query['base'], ':', rates['PLN'], query['symbols'])
    except requests.exceptions.ConnectTimeout:
        print('Timeout')