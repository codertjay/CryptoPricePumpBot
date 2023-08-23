import time

import ccxt

from utils import get_price_pair

# Initialize Poloniex API
exchange = ccxt.poloniex()

# Define the crypto pair
base_pair = 'USDT'
quote_pair = 'BTC'
symbol = f'{quote_pair}/{base_pair}'

# Initialize the previous price
previous_price = None

poloniex_trading_pairs = get_price_pair()

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
