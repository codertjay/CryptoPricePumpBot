import time

import ccxt

from telegram_notification import send_message_on_telegram

# Initialize Poloniex API
exchange = ccxt.poloniex()

# Define the crypto pair
base_pair = 'USDT'
quote_pair = 'BTC'
symbol = f'{quote_pair}/{base_pair}'

# Initialize the previous price
previous_price = None


def generate_chart_link(pair):
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


while True:
    # Fetch ticker data for the crypto pair
    ticker = exchange.fetch_ticker(symbol)

    # Get the current price
    current_price = ticker['last']

    # Calculate price change percentage if previous price exists
    if previous_price is not None:
        price_change_percentage = ((current_price - previous_price) / previous_price) * 100
        print(f"Price change percentage: {price_change_percentage:.2f}%")

        threshold = 30  # 30% increase
        if price_change_percentage >= threshold:
            send_notification(quote_pair, base_pair, price_change_percentage)

    # Update previous price
    previous_price = current_price

    # Wait for a specific interval before checking again
    time.sleep(5)  # Wait for 5 seconds before checking again
