import telebot
from parser import Generate
import TextCheck
import os


TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, введи одно слово на английском языке и я создам из него картинку!')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,
                     'Нужно ввести только одно слово на английском языке, в противном случае бот не создаст картинку '
                     'по вашему слову.\nПоддержать автора проекта: 410018159469941(Яндекс кошелек)')


@bot.message_handler(content_types=['text'])
def send_mend_photo(message):
    if TextCheck.check_en(message.text):
        mendeleev = Generate(word=message.text, user_id=message.from_user.first_name)
        mendeleev.split()
        img = mendeleev.make_jpg()
        bot.send_photo(message.chat.id, img)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, введите только одно слово на английском языке')


bot.polling(none_stop=True, interval=0)
