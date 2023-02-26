import os
import telebot
from telebot.types import Message
from flask import Flask, request
import logging

token = "5781580771:AAFe_HToFfz6QWgQVGJbj_YqTPCgwhmGPX8"
bot = telebot.TeleBot(token)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def start(message: Message):
    username = message.from_user.username
    bot.reply_to(message, f"Hello, {username}")


@server.route(f"/{token}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(f"http://92.255.67.180/{token}")
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

