import telebot
import requests
import threading
import time
import os
import TextCheck
from parser import split, make_jpg
from analytics import incoming

TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(TOKEN)

id_chat = os.environ["CHAT_ID"]


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, введи одно слово на английском языке и я создам из него картинку!')


@bot.message_handler(content_types=['text'])
def send_mend_photo(message):
    if TextCheck.check_en(message.text):
        imgs = split(message.text)
        img = make_jpg(imgs)
        bot.send_photo(message.chat.id, img)
        incoming(message.text, message.chat.id, message.chat.username)

    else:
        bot.send_message(message.chat.id, 'Пожалуйста, введите только одно слово на английском языке')


def req():
    while True:
        requests.get('https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + str(id_chat) + '&text=x')
        time.sleep(1500)


ping = threading.Thread(target=req)
ping.start()

bot.polling(none_stop=True, interval=0)
