import asyncio

import ccxt
from decouple import config

from telegram_notification import send_message_on_telegram


def get_futures_price_pairs():
    """
    Fetch futures price pairs involving the specified stable coin.
    :return: List of futures price pairs
    """
    # Define the base currency you're interested in (USDT)
    base_currency = config("BASE_CURRENCY")

    # Initialize the exchange API
    exchange = ccxt.poloniex({'option': {'defaultMarket': 'futures'}})

    # Fetch the futures markets data
    futures_markets = exchange.fetch_markets()

    # Find futures pairs with USDT as the base or quote currency
    usdt_futures_pairs = [market['symbol'] for market in futures_markets if base_currency in market['symbol']]

    return usdt_futures_pairs


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
              f"Previous Price {previous_price} \n" \
              f"Current Price {current_price} \n" \
              f"Previous Time {previous_time} \n" \
              f"Current Time {current_time} \n" \
              f"Increase Percentage: {increase_percentage:.2f}%\n" \
              f"Chart Link: {chart_link}"

    # send message for the pump
    asyncio.run(send_message_on_telegram(message))
    return
