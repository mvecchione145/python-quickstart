# --STEP LIST--
# 1. Run this script.
#     In your command line terminal window execute the following line:
#     python lesson-06.py

# 2. Comment out line 47 and uncomment line 48. Rerun this script.
#     In your command line terminal window execute the following line:
#     python lesson-06.py

import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint


def simple_html_get():
    response = requests.get('http://www.google.com')
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.title)

    for x in soup.findAll('a'):
        print(x)


def simple_json_get():
    ticker = 'AAPL'
    url = f'https://query1.finance.yahoo.com/v7/finance/chart/{ticker}'
    # url = 'https://query1.finance.yahoo.com/v7/finance/chart/{}'.format(ticker)
    # url = 'https://query1.finance.yahoo.com/v7/finance/chart/{ticker}'.format(ticker=ticker)
    # url = 'https://query1.finance.yahoo.com/v7/finance/chart/' + ticker

    # lines 28-31 do the same thing... f-strings are a python enhancement on python version 3

    response = requests.get(url)
    _json = json.loads(response.text)
    # _json = data.json()

    # lines 36-37 do the same thing... requests call returns a response object with a json method that will return a
    # dictionary object representation of the json (if the return is parse-able as json).

    print(_json)
    # pprint(_json)


if __name__ == "__main__":
    simple_html_get()
    # simple_json_get()



    # from datetime import datetime

    # closes = _json['chart']['result'][0]['indicators']['quote'][0]['close']
    # timestamps = _json['chart']['result'][0]['timestamp']

    # for c, t in zip(closes, timestamps):
        # print("DATE:")
        # print(f"    { datetime.fromtimestamp(t) }")
        # print("CLOSE PRICE:")
        # print(f"    { round(float(c), 2) if c else 0.0 }")
        # print()
        # print()
