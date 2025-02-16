import string
import random

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

'''
def bar(number):
    result = 0
    try:
        result = int(number)
    except ValueError:
        pass

    if not result:
        try:
            result = float(number)
        except ValueError:
            result = 'LoLo'

    return result
'''








'''
def bar(number):
    if number[0] == '+' and positive_number(number[1:]):
        #print('Первое слагаемое - положительное число типа int, начинается с символа +')
        a = int(number)
    elif number[0].isdigit() and positive_number(number):
        #print('Первое слагаемое - положительное число типа int.')
        a = int(number)
    elif number[0] == '-' and positive_number(number[1:]):
        #print('Первое слагаемое - отрицательное число типа int, начинается с символа -')
        a = int(number)
    elif number[0] == '+' and (delimeter_point1(number[1:]) or delimeter_point2(number[1:])):
        if delimeter_point2(number[1:]):
            number = number.replace(',', '.')
        #print("Первое слагаемое - положительное число типа float, начинается с символа +")
        a = float(number)
    elif number[0] == '-' and (delimeter_point1(number[1:]) or delimeter_point2(number[1:])):
        if delimeter_point2(number[1:]):
            number = number.replace(',', '.')
        #print('Первое слагаемое - отрицательное число типа float начинается с символа -')
        a = float(number)
    elif positive_number(number):
        #print('Первое слагаемое - положительное число типа int')
        a = int(number)
    elif delimeter_point1(number) or delimeter_point2(number):
        if delimeter_point2(number):
            number = number.replace(',', '.')
        #print('Первое слагаемое - положительное число типа float')
        a = float(number)
    else:
        a = number
    return a
'''

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
