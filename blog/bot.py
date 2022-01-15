from django.conf import settings

import telebot

bot = telebot.TeleBot(settings.BOT_TOKEN, parse_mode=None)

def send_feedback(text):
    bot.send_message(settings.CHAT_ID, text)