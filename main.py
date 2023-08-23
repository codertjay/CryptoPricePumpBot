import time

import ccxt

from utils import get_futures_price_pairs, send_notification

# Initialize Poloniex API
exchange = ccxt.poloniex()

# Initialize the previous price
previous_price = None

poloniex_trading_pairs = get_futures_price_pairs()

while True:
    # Fetch ticker data for the crypto pair
    for symbol in poloniex_trading_pairs:

        prices = {}
        # Define the crypto pair
        # mostly usdt which is the default pair we set
        base_pair = symbol.split("/")[1]
        # could be btc
        quote_pair = symbol.split("/")[0]

        ticker = exchange.fetch_ticker(symbol)
        # Get the current price
        current_price = ticker['last']
        # set  the old price
        old_price = prices[ticker["id"]]
        prices[ticker["id"]] = ticker['last']
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
