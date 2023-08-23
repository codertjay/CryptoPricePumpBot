# Crypto Price Pump Detection Bot

This is a Python bot that monitors cryptocurrency price pairs involving a specified stablecoin and sends notifications via Telegram for price pumps exceeding a certain threshold.

## Features

- Monitors cryptocurrency price pairs involving a specified stablecoin (e.g., USDT).
- Detects price pumps exceeding a specified threshold percentage.
- Sends price pump notifications to a Telegram user.

## Prerequisites

- Python 3.x
- `ccxt` library
- `decouple` library
- Telegram API token and chat ID (for sending notifications)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/codertjay/PricePumpBot.git
   cd PricePumpBot
