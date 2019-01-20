# Coin prices
Requests crypto prices from coinmarketcap.com and prints them to `stdout` in the
format required for a `ledger` price history database.

At the moment, it's hardcoded to request quotes for ADA, BTC, LTC, XRP, and ETH
in AUD, because that's all that's relevant to me. Maybe I'll update it later on
to make it more flexible.

## Requirements
Python 3.6+ (uses `f` strings, hence 3.6)
pip
CoinMarketCap API key in environment variable `COIN_MARKET_CAP_API_KEY`

## Installation
Clone the repo.

Install requirements:
```bash
pip install -r requirements.txt
```

## Usage:
```bash
python coinprices.py
```

I like to append this to my price history. For example:
```bash
python coinprices.py >> ~/.pricedb
```

It's nice to set this up in a cronjob for whatever frequency works for you.

## License
MIT
