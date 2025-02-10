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
    bot.send_message(message.chat.id, "Напиши два числа церез пробел, а я посчитаю их сумму.")
    print("Бот ответил: Напиши два числа церез пробел, а я посчитаю их сумму.\n")

@bot.message_handler(commands=['help'])
def help_command(message):
    monitoring_standard(message)
    commands = ('/start', '/help', '/samsa')
    #print(message.text)
    help_message = "Привет! Я очень простой бот, "\
                "пока я умею только складывать два числа. "\
                "Но очень скоро, когда я вырасту, у меня появится больше умений! "\
                "И тогда я смогу приносить больше пользы!\n\n"\
                "Вот список команд, которые мне доступны:\n/start\n/help\n/samsa"
    bot.send_message(message.chat.id, help_message)
    print(f"Бот ответил: {help_message}\n")

@bot.message_handler(commands=['samsa'])
def samsa_command(message):
    monitoring_standard(message)
    #print(message.text)
    bot.send_message(message.chat.id, "Такая команда samsa называется. Ничего не делает.")
    bot.send_message(message.chat.id, "Это сообщение отправляется пользователю.")
    w = message.chat.id
    bot.send_message(message.chat.id, w)

@bot.message_handler(content_types = ['text'])
def text_message(message):
    monitoring_standard(message)
    #print(message.text)
    if message.text.lower() == 'привет':
        #bot.send_message(message.chat.id, str(sum([int(num) for num in message.text.split()])))
        bot.send_message(message.chat.id, "Приветствую тебя!")
        print("Бот ответил: Приветствую тебя!")
    elif len(message.text.split()) == 2:
        number_a, number_b = message.text.split()
        answer = tbot_2_lib.bar(number_a) + tbot_2_lib.bar(number_b)
        bot.send_message(message.chat.id, answer)
        print(f"Бот ответил: {answer}\n")
        #bot.send_message(message.chat.id, str(float(message.text.split()[0]) + float(message.text.split()[1])))
        #print(f"Бот ответил: {str(float(message.text.split()[0]) + float(message.text.split()[1]))}\n")
    else:
        bot.send_message(message.chat.id, "Не понимаю о чем ты. Ведь я еще очень маленький бот.\n"
                                          "Напиши /help для справки.")
        print("Бот ответил: Не понимаю о чем ты. Ведь я еще очень маленький бот.\n"
              "             Напиши /help для справки.\n")

bot.polling()
