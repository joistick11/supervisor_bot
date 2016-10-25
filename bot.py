import telebot
import settings
from google import search
import google
import urllib.request as urllib2


bot = telebot.TeleBot(settings.token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('фото', 'аудио')
    bot.send_message(message.chat.id,"Привет! Желаешь найти что-нибудь?", reply_markup=user_markup)

@bot.message_handler(commands=['найти'])
def handle_search(message):
    i = 0
    bot.send_message(message.chat.id, "По запросу " + message.text[7:] + " я нашел это:")
    for url in search(message.text[7:], stop=1):
        bot.send_message(message.chat.id, url)
        i = i + 1
        if i == 5:
            break
    bot.send_message(message.chat.id, "Хотите найти еще что-нибудь?")
    #bot.send_message(message.chat.id, message.text[7:])

@bot.message_handler(commands=['покажи'])
def handle_show(message):
    if message.text[8:] == 'кошку' or message.text[8:] == 'кота' or message.text[8:] == 'котят':
        img1 = open('cat1.jpg', 'rb')
        img2 = open('cat2.jpg', 'rb')
        img3 = open('cat3.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'upload_photo')
        bot.send_photo(message.chat.id, img1)
        img1.close()
        bot.send_photo(message.chat.id, img2)
        img2.close()
        bot.send_photo(message.chat.id, img3)
        img3.close()
    elif message.text[8:] == 'автомобиль' or message.text[8:] == 'машину':
        img1 = open('car1.jpg', 'rb')
        img2 = open('car2.jpg', 'rb')
        img3 = open('car3.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'upload_photo')
        bot.send_photo(message.chat.id, img1)
        img1.close()
        bot.send_photo(message.chat.id, img2)
        img2.close()
        bot.send_photo(message.chat.id, img3)
        img3.close()
    elif message.text[8:] == 'космос' or message.text[8:] == 'галактику':
        img1 = open('space1.jpg', 'rb')
        img2 = open('space2.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'upload_photo')
        bot.send_photo(message.chat.id, img1)
        img1.close()
        bot.send_photo(message.chat.id, img2)
        img2.close()
    elif message.text[8:] == 'природу':
        img1 = open('nature1.jpg', 'rb')
        img2 = open('nature2.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'upload_photo')
        bot.send_photo(message.chat.id, img1)
        img1.close()
        bot.send_photo(message.chat.id, img2)
        img2.close()
    elif message.text[8:] == 'программиста':
        img1 = open('programmer1.jpg', 'rb')
        img2 = open('programmer2.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'upload_photo')
        bot.send_photo(message.chat.id, img1)
        img1.close()
        bot.send_photo(message.chat.id, img2)
        img2.close()




@bot.message_handler(content_types=["text"])
def search_message(message):
    if message.text == 'фото' or message.text == 'аудио':
        i = 0
        bot.send_message(message.chat.id, "По запросу " + message.text + " я нашел это:")
        for url in search(message.text, stop=1):
            bot.send_message(message.chat.id, url)
            i = i + 1
            if i == 5:
                break



if __name__ == '__main__':
    bot.polling(none_stop=True)