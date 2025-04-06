import string
import random
import psycopg
import os
from dotenv import load_dotenv


def positive_number(number):
    flag = 1
    for digit in number:
        if digit in string.digits:
            flag *= 1
        else:
            flag *= 0
    return flag


def delimeter_point1(number):
    flag = 0
    if number.count('.') == 1:
        if 0 < number.index('.') < len(number):
            flag = 1
    return flag


def delimeter_point2(number):
    flag = 0
    if number.count(',') == 1:
        if 0 < number.index(',') < len(number):
            flag = 1
    return flag


def bar(number):
    if delimeter_point1(number) or delimeter_point2(number):
        if delimeter_point2(number):
            number = number.replace(',', '.')
        try:
            result = float(number)
        except ValueError:
            result = rnd_text()
    else:
        try:
            result = int(number)
        except ValueError:
            result = rnd_text()
    return result


load_dotenv()
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")


def postgres_add_line(text):
    connect = psycopg.connect(host=db_host, port=5432, user=db_user, password=db_password, dbname=db_name)
    cursor = connect.cursor()
    cursor.execute("INSERT INTO tbot2log (datetime, username, question, answer) VALUES (%s, %s, %s, %s);", text)
    connect.commit()
    cursor.close()
    connect.close()


def rnd_text():
    words = ["Что-то тут не так. Попробуй снова.\nИли напиши /help для справки.",
             "Не совсем понимаю о чем ты.\nНапиши /help для справки.",
             "Здесь явно что-то не то.\nПопробуй напиши /help для справки."]
    return random.choice(words)


def add_number(number_a, number_b):
    if type(bar(number_a)) in [int, float] and type(bar(number_b)) in [int, float]:
        result = bar(number_a) + bar(number_b)
    else:
        result = rnd_text()
    return result
