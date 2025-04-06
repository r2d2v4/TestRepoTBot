import telebot
import tbot_2_lib
import os
from dotenv import load_dotenv
from datetime import datetime as dt


load_dotenv()

token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)


def monitoring_standard(message):
    return [dt.fromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S'), message.from_user.username[:100], message.text[:255]]


@bot.message_handler(commands=['start'])
def start_message(message):
    start_message = "Напиши два числа церез пробел, а я посчитаю их сумму."
    bot.send_message(message.chat.id, start_message)
    hello = monitoring_standard(message)
    hello.append(start_message)
    tbot_2_lib.postgres_add_line(hello)

@bot.message_handler(commands=['help'])
def help_command(message):
    hello = monitoring_standard(message)
    help_message = "Вот список команд, которые мне доступны:\n/start\n/help\n/about"
    bot.send_message(message.chat.id, help_message)
    hello.append(help_message.replace("\n", " "))
    tbot_2_lib.postgres_add_line(hello)

@bot.message_handler(commands=['about'])
def samsa_command(message):
    hello = monitoring_standard(message)
    about_message = "Привет! Я очень простой бот, "\
                    "пока я умею только складывать два числа. "\
                    "Но очень скоро, когда я вырасту, у меня появится больше умений! "\
                    "И тогда я смогу приносить больше пользы! "\
                    "Давай попробуем! /start"
    bot.send_message(message.chat.id, about_message)
    hello.append(about_message.replace("\n", " "))
    tbot_2_lib.postgres_add_line(hello)

@bot.message_handler(content_types = ['text'])
def text_message(message):
    hello = monitoring_standard(message)
    if message.text.lower() == 'привет':
        hello_message = "Приветствую тебя! Давай начнём! /start"
        bot.send_message(message.chat.id, hello_message)
        hello.append(hello_message.replace("\n", " "))
        tbot_2_lib.postgres_add_line(hello)
    elif len(message.text.split()) == 2:
        number_a, number_b = message.text.split()
        answer = tbot_2_lib.add_number(number_a, number_b)
        bot.send_message(message.chat.id, answer)
        hello.append(str(answer)[:255].replace("\n", " "))
        tbot_2_lib.postgres_add_line(hello)
    else:
        other_message = tbot_2_lib.rnd_text()
        bot.send_message(message.chat.id, other_message)
        hello.append(other_message.replace("\n", " "))
        tbot_2_lib.postgres_add_line(hello)

#bot.polling(none_stop=True, interval=0)
bot.polling()
