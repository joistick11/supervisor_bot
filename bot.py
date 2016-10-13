# -*- coding: utf-8 -*-
import telebot as tb
import settings
import time
import botDB
import logging

bot = tb.TeleBot(settings.token)
logger = tb.logger
tb.logger.setLevel(logging.ERROR)


def save_new_user(message):
    botDB.store_new_user_into_db(message.from_user.id,
                                 message.from_user.username,
                                 message.from_user.first_name,
                                 message.from_user.last_name)
    pass


def check_user_exists(message):
    return botDB.check_user_id_exists(message.from_user.id)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username
    if check_user_exists(message):  # if the username exists in our database
        # save_chat_id(message.chat_id, username)
        reply = 'Hello {0}, how are you? Nice to meet you again'.format(username)
    else:
        save_new_user(message)
        reply = '{0}, first time? Huh'.format(username)
    bot.reply_to(message, reply)


if __name__ == '__main__':
    bot.polling()
