from telegram import Bot
from decouple import config


def send_message_on_telegram(message):
    """
    the message to be sent on telegram
    :param message:
    :return:
    """
    # Replace 'YOUR_BOT_TOKEN' with the actual token you obtained from BotFather
    bot = Bot(token=config("TELEGRAM_BOT_TOKEN", default=""))

    # Replace 'YOUR_CHAT_ID' with your own chat ID
    chat_id = config("TELEGRAM_CHAT_ID", default="")

    # Replace 'Your message here' with the message you want to send

    bot.send_message(chat_id=chat_id, text=message)
    return True
