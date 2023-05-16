import requests
from bs4 import BeautifulSoup
import json

stocks = ['VAST.L', 'ICON.L', 'PREM.L', 'BZT.L']
stockdata = []


def getData(ticker: str) -> list:
    """Gets data from YahooFinance and return an JSON"""
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'}
    url = f"https://finance.yahoo.com/quote/{ticker}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
        'price': soup.find('div', {'class': 'D(ib) Mend(20px)'})
        .find_all('fin-streamer')[0].text,
        'change': soup.find('div', {'class': 'D(ib) Mend(20px)'})
        .find_all('fin-streamer')[1].text,
        }
    return stock


for item in stocks:
    stockdata.append(getData(item))
    print(f'Downloading: {item}...')

with open('stockdata.json', 'w') as f:
    json.dump(stockdata, f)
