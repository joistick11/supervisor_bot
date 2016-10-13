# -*- coding: utf-8 -*-
import telebot as tb
import settings
import time
import botDB
import logging

bot = tb.TeleBot(settings.token)
logger = tb.logger
tb.logger.setLevel(logging.DEBUG)


def extract_unique_code(text):
    """
        Extracts the unique code from the sent '/start' command
    """
    return text.split()[1] if len(text.split()) > 1 else None


def in_storage(user_id):
    # TODO: Should check if unique code exists in storage
    botDB.check_user_id(user_id)
    pass


def get_username_from_storage(user_id):
    # TODO: Does a query to the storage, retrieving the assosiated username
    # FIXME: Should be replaced with real database lookup
    botDB.get_username_by_id(user_id)
    return "ABC" if in_storage(user_id) else None


def save_chat_id(chat_id, username):
    # TODO: Save chat_id->username to storage

    pass


@bot.message_handler(commands=['start'])
def send_welcome(message):
    unique_code = extract_unique_code(message.text)
    if unique_code:
        username = get_username_from_storage(unique_code)
        if username:  # if the username exists in our database
            save_chat_id(message.chat_id, username)
            reply = 'Hello {0}, how are you?'.format(username)
        else:
            reply = 'I have no clue who you are'
    else:
        reply = 'Please visit me via a provided URL from the website.'
    bot.reply_to(message, reply)


if __name__ == '__main__':
    bot.polling()
