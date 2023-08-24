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

2 **Setting Up a Virtual Environment**:

   If you haven't already, you can set up a virtual environment to isolate your project's dependencies. This helps avoid conflicts with other projects and keeps your environment clean.

   ```bash
   # Create a new virtual environment (replace 'venv' with your preferred name)
   python -m venv venv

   # Activate the virtual environment
   # On Windows
   venv\Scripts\activate
   # On macOS and Linux
   source venv/bin/activate
   ```

3 **Installing Dependencies from `requirements.txt`**:

   If you have a `requirements.txt` file that lists all your project's dependencies, you can install them using the following command:

   ```bash
   pip install -r requirements.txt
   ```

   Make sure you've navigated to your project directory before running this command.

4. **Update .env or Create a new .env file with the sample provided .
5. R