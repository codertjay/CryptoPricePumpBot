import datetime
import time

import ccxt
from decouple import config

from utils import get_futures_price_pairs, send_notification

# Initialize Poloniex API
exchange = ccxt.poloniex()

# Get the trading pairs
poloniex_trading_pairs = get_futures_price_pairs()
#  the price pairs
prices = {}
# the last time it ran for that pair
price_durations = {}

while True:
    # Fetch ticker data for the crypto pair
    # Record the start time
    start_time = time.time()
    for symbol in poloniex_trading_pairs:

        # Define the crypto pair
        # mostly usdt which is the default pair we set
        base_pair = symbol.split("/")[1]
        # could be btc
        quote_pair = symbol.split("/")[0]

        ticker = exchange.fetch_ticker(symbol)
        # Get the current price
        current_price = ticker['last']
        # Get the previous price
        previous_price = prices.get(ticker["id"])
        # set the price
        prices[ticker["id"]] = ticker['last']

        # Time
        current_time = datetime.datetime.now()
        previous_time = price_durations.get(ticker["id"])
        # set the duration
        price_durations[ticker["id"]] = current_time

        # Calculate price change percentage if previous price exists
        print(f"Trading Pair: {symbol}. Current Price: {current_price}, Previous Price: {previous_price}")
        if previous_price is not None:
            price_change_percentage = ((current_price - previous_price) / previous_price) * 100
            print(f"Price change percentage: {price_change_percentage:.2f}%")

            threshold = config("PUMP_PERCENT", cast=int, default=30)  # 30% increase
            if price_change_percentage >= threshold:
                send_notification(pair=symbol, increase_percentage=price_change_percentage,
                                  previous_price=previous_price, current_price=current_price,
                                  current_time=current_time,
                                  previous_time=previous_time,
                                  )

        # Update previous price
        previous_price = current_price

        # Wait for a specific interval before checking again
        # time.sleep(5)  # Wait for 5 seconds before checking again
    # Record the end time
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    # sleep for  minute
    time.sleep(config("SLEEP_TIME", cast=int, default=0))
