import telebot
import tbot_2_lib
import os
from dotenv import load_dotenv


load_dotenv()

token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)

def monitoring_standard(message):
    print(f"Пользователь: {message.from_user.username}")  # это интересно :)
    print(f"Ввел текст: {message.text}")

@bot.message_handler(commands=['start'])
def start_message(message):
    monitoring_standard(message)
    start_message = "Напиши два числа церез пробел, а я посчитаю их сумму."
    bot.send_message(message.chat.id, start_message)
    print(f"Бот ответил: {start_message}\n")

@bot.message_handler(commands=['help'])
def help_command(message):
    monitoring_standard(message)
    help_message = "Вот список команд, которые мне доступны:\n/start\n/help\n/about"
    bot.send_message(message.chat.id, help_message)
    print(f"Бот ответил: {help_message}\n")

@bot.message_handler(commands=['about'])
def samsa_command(message):
    monitoring_standard(message)
    about_message = "Привет! Я очень простой бот, "\
                    "пока я умею только складывать два числа. "\
                    "Но очень скоро, когда я вырасту, у меня появится больше умений! "\
                    "И тогда я смогу приносить больше пользы!"\
                    "Давай попробуем! /start"
    bot.send_message(message.chat.id, about_message)
    print(f"Бот ответил: {about_message}\n")

@bot.message_handler(content_types = ['text'])
def text_message(message):
    monitoring_standard(message)
    if message.text.lower() == 'привет':
        hello_message = "Приветствую тебя! Давай начнём! /start"
        bot.send_message(message.chat.id, hello_message)
        print(f"Бот ответил: {hello_message}\n")
    elif len(message.text.split()) == 2:
        number_a, number_b = message.text.split()
        answer = tbot_2_lib.add_number(number_a, number_b)
        bot.send_message(message.chat.id, answer)
        print(f"Бот ответил: {answer}\n")

    else:
        other_message = tbot_2_lib.rnd_text()
        bot.send_message(message.chat.id, other_message)
        print(f"Бот ответил: {other_message}\n")

bot.polling(none_stop=True, interval=0)
