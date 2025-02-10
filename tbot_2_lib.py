import string


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
    if number[0] == '+' and positive_number(number[1:]):
        print('Первое слагаемое - положительное число типа int, начинается с символа +')
        a = int(number)
    elif number[0].isdigit() and positive_number(number):
        print('Первое слагаемое - положительное число типа int.')
        a = int(number)
    elif number[0] == '-' and positive_number(number[1:]):
        print('Первое слагаемое - отрицательное число типа int, начинается с символа -')
        a = int(number)
    elif number[0] == '+' and (delimeter_point1(number[1:]) or delimeter_point2(number[1:])):
        if delimeter_point2(number[1:]):
            number = number.replace(',', '.')
        print("Первое слагаемое - положительное число типа float, начинается с символа +")
        a = float(number)
    elif number[0] == '-' and (delimeter_point1(number[1:]) or delimeter_point2(number[1:])):
        if delimeter_point2(number[1:]):
            number = number.replace(',', '.')
        print('Первое слагаемое - отрицательное число типа float начинается с символа -')
        a = float(number)
    elif positive_number(number):
        print('Первое слагаемое - положительное число типа int')
        a = int(number)
    elif delimeter_point1(number) or delimeter_point2(number):
        if delimeter_point2(number):
            number = number.replace(',', '.')
        print('Первое слагаемое - положительное число типа float')
        a = float(number)
    return a


#numbers = input('Введите два числа через пробел:\n')
'''
if len(numbers.split()) == 2:
    number_a, number_b = numbers.split()
    #print(number_a)
    #print(number_b)
    print(bar(number_a) + bar(number_b))
'''
