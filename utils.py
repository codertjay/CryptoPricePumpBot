import asyncio
import time

import ccxt
import requests
from decouple import config

from telegram_notification import send_message_on_telegram


def get_futures_price_pairs():
    """
    Fetch futures price pairs involving the specified stable coin with a minimum 24-hour volume.
    :return: List of futures price pairs
    """
    # Define the base currency you're interested in (USDT)
    base_currency = config("BASE_CURRENCY")
    # Minimum volume
    min_volume = config("MINIMUM_VOLUME", cast=float, default=0)

    # Initialize the exchange API
    exchange = ccxt.poloniex({'option': {'defaultMarket': 'futures'}})

    # Fetch the futures markets data
    # futures_markets = exchange.fetch_markets()
    response = requests.get("https://api.poloniex.com/markets/ticker24h")

    if response.status_code != 200:
        return
    futures_markets = response.json()

    # List to store relevant pairs
    relevant_futures_pairs = []

    print("Getting Market volume .... This could take some time")
    # Fetch additional data for each relevant market (including volume)
    for market_info in futures_markets:
        if base_currency in market_info['symbol']:
            market_id = market_info['symbol']
            # market_info = exchange.fetch_ticker(market_id)
            market_info['amount'] = market_info['amount']  # Add quoteVolume directly to market data
            print(f"Market Volume for {market_id} is {market_info['amount']}")

            if float(market_info['amount']) <= float(min_volume):
                relevant_futures_pairs.append(market_info['displayName'])

    print("================================================================")
    print(f"Token that pass minimum volumes  {min_volume} are {len(relevant_futures_pairs)}")
    print("================================================================")
    time.sleep(3)
    return relevant_futures_pairs


def generate_chart_link(pair):
    """
    this is used to generate a link for the pair  which would be for sending to telegram
    :param pair:
    :return:
    """
    # Construct the trading pair symbol
    symbol = pair.replace("/", "_")
    # Generate the link to the live chart
    chart_link = f'https://poloniex.com/trade/{symbol}'
    return chart_link


def send_notification(pair, increase_percentage, previous_price, current_price, current_time, previous_time):
    """
    send the  message to the user telegram which is being set on the .env
    :param pair:
    :param increase_percentage:
    :return:
    """
    chart_link = generate_chart_link(pair)

    message = f"Price pump detected for {pair}!\n" \
              f"Current Price {current_price} \n" \
              f"Previous Price {previous_price} \n" \
              f"Current Time {current_time} \n" \
              f"Previous Time {previous_time} \n" \
              f"Increase Percentage: {increase_percentage:.2f}%\n" \
              f"Chart Link: {chart_link}"

    # send message for the pump
    asyncio.run(send_message_on_telegram(message))
    return
