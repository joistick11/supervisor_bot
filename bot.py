import telebot
# Установить telebot: Заходим в Командную строку Windows
#  pip install telebot
import settings

# Адрес нашего бота: telegram.me/science_supervisor_bot

bot = telebot.TeleBot(settings.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
