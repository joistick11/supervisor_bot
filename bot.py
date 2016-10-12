import telepot
import settings
import time


# Адрес нашего бота: telegram.me/science_supervisor_bot

def handle(msg):
    flavor = telepot.flavor(msg)
    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)


TOKEN = settings.token

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print('Listening...')

while 1:
    time.sleep(10)
