import ccxt
from decouple import config

from telegram_notification import send_message_on_telegram


def get_price_pair():
    """
    the base currency could change to any stable coin  notation
    :return:
    """
    # Define the base currency you're interested in (USDT)
    base_currency = config("BASE_CURRENCY")

    # Initialize Poloniex API
    exchange = ccxt.poloniex()

    # Fetch the exchange markets
    markets = exchange.load_markets()
    # Find all pairs with USDT as the base or quote currency
    usdt_pairs = [pair for pair, info in markets.items() if base_currency in info['symbol']]
    return usdt_pairs


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


def send_notification(pair, increase_percentage):
    """
    send the  message to the user telegram which is being set on the .env
    :param pair:
    :param increase_percentage:
    :return:
    """
    chart_link = generate_chart_link(pair)

    message = f"Price pump detected for {pair}!\n" \
              f"Increase Percentage: {increase_percentage:.2f}%\n" \
              f"Chart Link: {chart_link}"

    # send message for the pump
    send_message_on_telegram(message)
    return
