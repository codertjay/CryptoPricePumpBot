import requests
from aiogram import Bot
from decouple import config
from telegram import Bot


def get_chat_id():
    """
    this is used to get the list of chat id a user have for you to be able to set it when sending message
    :return:
    """
    bot_token = config("TELEGRAM_BOT_TOKEN")
    response = requests.get(f"https://api.telegram.org/bot{bot_token}/getUpdates")
    data = response.json()

    if "result" in data and len(data["result"]) > 0:
        chat_id = data["result"][0]["message"]["chat"]["id"]
        print("Chat ID:", chat_id)
    else:
        print("No chat data found.")


async def send_message_on_telegram(message):
    """
    Send the message to be sent on Telegram.
    :param message: The message to send.
    """
    # Replace 'YOUR_BOT_TOKEN' with the actual token you obtained from BotFather
    bot = Bot(token=config("TELEGRAM_BOT_TOKEN"))

    # Replace 'YOUR_CHAT_ID' with your own chat ID
    chat_id = config("TELEGRAM_CHAT_ID")

    await bot.send_message(chat_id=chat_id, text=message)

