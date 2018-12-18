from math import sin, cos, tan


def add(a, b):  # функция сложения
    return a + b


def sub(a, b):  # функция вычитания
    return a - b


def mult(a, b):  # функция умножения
    return a * b


def div(a, b):  # функция деления
    try:
        return a / b
    except ZeroDivisionError as err:
        print('Ошибка при делении на 0 >>>', err)


def int_div(a, b):  # функция целочисленного деления
    try:
        return a // b
    except ZeroDivisionError as err:
        print('Ошибка при делении на 0 >>>', err)


def ostatok_ot_div(a, b):  # функция остатка от деления
    try:
        return a % b
    except ZeroDivisionError as err:
        print('Ошибка при делении на 0 >>>', err)


def exponentiation(a, b):  # функция возведение в степень
    return a ** b


def sinus(a, b=None):  # функция нахождения синуса
    return sin(a)


def cosinus(a, b=None):  # функция нахождения косинуса
    return cos(a)


def tangent(a, b=None):  # функция нахождения тангенса
    return tan(a)
