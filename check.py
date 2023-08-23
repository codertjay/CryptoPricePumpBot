import ccxt
from decouple import config

# Define the base currency you're interested in (USDT)
base_currency = config("BASE_CURRENCY")


def get_price_pair(base_currency):
    """
    the base currency could change to any stable coin  notation
    :param base_currency: The currency pair we are checking for
    :return:
    """
    # Initialize Poloniex API
    exchange = ccxt.poloniex()

    # Fetch the exchange markets
    markets = exchange.load_markets()
    # Find all pairs with USDT as the base or quote currency
    usdt_pairs = [pair for pair, info in markets.items() if base_currency in info['symbol']]
    return usdt_pairs
