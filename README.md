# Coin prices
Requests crypto prices from coinmarketcap.com and prints them to `stdout` in the
format required for a `ledger` price history database.

Perhaps somewhat confusingly, I'm refering to the ledger accounting software
(https://www.ledger-cli.org/), not the Ledger hardware wallet (https://www.ledger.com/), although I do use and recommend both!

At the moment, it's hardcoded to request quotes for ADA, BTC, LTC, XRP, and ETH
in AUD, because that's all that's relevant to me. Maybe I'll update it later on
to make it more flexible.

## Requirements
* Python 3.6+ (uses `f` strings, hence 3.6)
* pip
* CoinMarketCap API key in environment variable `COIN_MARKET_CAP_API_KEY`

## Installation
Clone the repo.

Install requirements:
```sh
pip install -r requirements.txt
```

## Usage:
```sh
python coinprices.py
```

I like to append the output to my price history. For example:
```sh
python coinprices.py >> ~/.pricedb
```

It's nice to set this up in a cronjob for whatever frequency works for you.

## License
MIT
