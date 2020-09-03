import requests
import json

def stats(function):
    def inside():
        function()
    return inside()

@stats
def exchange_rate():
    try:
        query = {'base': 'USD', 'symbols': 'PLN'}
        r = requests.get('https://api.exchangeratesapi.io/latest', params=query)
        response_dictionary = json.loads(r.content)
        rates = response_dictionary['rates']
        print('Kurs dolara: ', rates['PLN'])
    except requests.exceptions.ConnectTimeout:
        print('Timeout')