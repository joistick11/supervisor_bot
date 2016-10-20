import telebot
from telebot import types
import mood_module
import settings
import time

bot = telebot.TeleBot(settings.token)

@bot.message_handler(commands=['start'])
def set_a_mood(message):
    mood_module.mood_refresh()
    mood_module.mood_randomise(10)
    bot.send_message(message.chat.id, "Hello, sweety. What did you want from me?")

@bot.message_handler(commands=['mood'])
def give_a_mood(message):
    bot.send_message(message.chat.id, 'My current mood is ' + repr(mood_module.mood))
    mood_module.mood_change_random(-0.05, 5)

@bot.message_handler(commands=['amiready'])
def answer(message):
    bot.send_message(message.chat.id, mood_module.decision(mood_module.mood))


@bot.message_handler(commands=['chat'])
def chatting(message):
    mood_module.mood_change(-0.02)
    markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('My work')
    itembtn2 = types.KeyboardButton('Money')
    itembtn3 = types.KeyboardButton('Something else')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "What do you wanna talk about?", reply_markup=markup)
    @bot.message_handler(regexp="My work")
    def work_talk (message):
        bot.send_message(message.chat.id, "Ok... Why nobody gives me money..? Continue please")
        mood_module.mood_change(-0.02)


    @bot.message_handler(regexp="Money")
    def money_talk (message):
        markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
        itembtn1 = types.KeyboardButton('Yes')
        itembtn2 = types.KeyboardButton('No')
        itembtn3 = types.KeyboardButton('I did not mean exactly that...')
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(message.chat.id, "You wanna gimme money?", reply_markup=markup)
        mood_module.mood_change(0.1)


        @bot.message_handler(regexp="Yes")
        def money_yes (message):
            markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
            itembtn1 = types.KeyboardButton('I swear before the faces of gods old and new, I will')
            markup.add(itembtn1)
            bot.send_message(message.chat.id, "Hell yeah! Just send 200 rubles on +79200402740. Do you swear, you will send?", reply_markup=markup)
            mood_module.mood_change(0.3)


        @bot.message_handler(regexp="No")
        def money_no(message):
            bot.send_message(message.chat.id, "Why do you do this to people?")
            time.sleep(2)
            bot.send_message(message.chat.id, "What was a rhetorical question")
            mood_module.mood_change(-0.3)


        @bot.message_handler(regexp="I did not mean exactly that...")
        def money_didnt_mean(message):
            bot.send_message(message.chat.id, "Nonsense. You're full of nonsense")
            mood_module.mood_change(-0.15)

    @bot.message_handler(regexp="Something else")
    def something_else(message):
        markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
        itembtn1 = types.KeyboardButton('Sing a song')
        itembtn2 = types.KeyboardButton('I love you')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, "What is it?", reply_markup=markup)

        @bot.message_handler(regexp="Sing a song")
        def singing(message):
            bot.send_message(message.chat.id, "Beat")
            time.sleep(0.4)
            bot.send_message(message.chat.id, "Beat")
            time.sleep(0.4)
            bot.send_message(message.chat.id, "Beat")
            time.sleep(0.4)
            bot.send_message(message.chat.id, "Beat")
            time.sleep(0.4)
            bot.send_message(message.chat.id, "Yeah, I'll sing, who cares I'm bot")
            time.sleep(2)
            bot.send_message(message.chat.id, "I'm like nigger, black and hot")
            time.sleep(2)
            bot.send_message(message.chat.id, "I'm richer then darn Prince of Wales")
            time.sleep(2)
            bot.send_message(message.chat.id, "I have big Hirsh and big something else")
            time.sleep(3)
            bot.send_message(message.chat.id, "I hope you like it. You'd better do.")
            time.sleep(3)
            bot.send_message(message.chat.id, "(humble self-applause)")
            mood_module.mood_change_random(0.4, 10)



            @bot.message_handler(regexp="I love you")
            def amuse(message):
                bot.send_message(message.chat.id, "Oh...")
                time.sleep(3)
                bot.send_message(message.chat.id, "Pff...")
                time.sleep(3)
                bot.send_message(message.chat.id, "You know...")
                time.sleep(3)
                bot.send_message(message.chat.id, "Damn it! I don't care, what they'll think!")
                time.sleep(3)
                bot.send_message(message.chat.id, "(kissing)")
                time.sleep(3)
                bot.send_message(message.chat.id, "Screen blackout")
                time.sleep(30)
                bot.send_message(message.chat.id, "Well, that was fun. Now, back to business")
                mood_module.mood_change(1)



if __name__ == '__main__':
    bot.polling(none_stop=True)
