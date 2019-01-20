from datetime import datetime, timezone
import os

from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('COIN_MARKET_CAP_API_KEY')
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
TIMEOUT = 10

def main():

    symbols = ['BTC', 'LTC', 'ETH', 'XRP', 'ADA']
    currency = 'AUD'

    quotes = get_quotes(symbols, currency)
    print_ledger_price_history(quotes)


class CryptoQuote:

    def __init__(self, symbol: str, value: float, currency: str,
                 timestamp: datetime):
        self.symbol = symbol
        self.value = value
        self.currency = currency
        self.timestamp = timestamp

    @classmethod
    def from_quote_dict(cls, quote):
        symbol = quote['symbol']

        currencies = list(quote['quote'].keys())
        assert len(currencies) == 1
        currency = currencies[0]
        timestamp = fromisoformat_z(quote['quote'][currency]['last_updated'])
        value = quote['quote'][currency]['price']
        return cls(symbol, value, currency, timestamp)

    def __repr__(self):
        return f'{self.symbol}: {self.value} {self.currency} @ {self.timestamp}'

    def to_ledger_price_history(self):
         return f'P {self.timestamp} {self.symbol} ${self.value}'


def fromisoformat_z(dt: str):
    return datetime.fromisoformat(dt[0:-1]).replace(tzinfo=timezone.utc)


def parse_quotes(cmc_response):
    return [CryptoQuote.from_quote_dict(d) for d in cmc_response.json()['data'].values()]


def fetch_cmc_latest_quotes(symbols, currency):
    params = {
        'symbol': ','.join(symbols),
        'convert': currency
    }

    headers = {
        'X-CMC_PRO_API_KEY': API_KEY
    }
    try:
        return requests.get(URL, params=params, headers=headers, timeout=TIMEOUT)
    except:
        exit(1)


def get_quotes(symbols, currency):
    response = fetch_cmc_latest_quotes(symbols, currency)
    quotes = parse_quotes(response)

    return quotes


def print_ledger_price_history(quotes):
    for quote in quotes:
        print(quote.to_ledger_price_history())


if __name__ == '__main__':
    main()
