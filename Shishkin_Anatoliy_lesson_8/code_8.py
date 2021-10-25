# Регулярные выражения и декораторы в Python
import re


RE_NAME = re.compile(r'^[А-ЯЁ][а-яё]+$')
WRONG = False
RE_DATE = re.compile(r'^(\d{2}.){2}\d{4}$') if WRONG else re.compile(r'^(\d{1,2}\.){2}\d{4}$')
RE_DATE_2 = re.compile(r'^(\d{2}[./\-,~\\?]){2}\d{4}$')

# match
# for date in ['23.01.2021', '23,01,2021', '23~01~2021', '23?01?2021', '23-01-2021', r'23\01\2021']:
#     assert RE_DATE_2.match(date), f'wrong date {date}'


# findall
# RE_DATE_3 = re.compile(r'(?:\d{2}[.-/]){2}\d{4}')  # обратите внимание на "?:"
RE_DATE_3 = re.compile(r'(?:\d{2}[+-/]){2}\d{4}')  # обратите внимание на "?:"


txt = 'Погода 23.01.2021 была отличная! Зато за день до этого (22/01/2021) - очень холодно. ' \
      'Надеемся, что 24-01-2021 будет без ветра. 24,01,2021'

print(RE_DATE_3.findall(txt))

own_text = """
    ВНИМАНИЕ! 25.10.2021 состоится вебинарное занятие по теме "Регулярные выражения и декораторы в Python"
    Всем рекомендуется сдать практические задания по прошлому занятию до 24-10-2021, а по проводимому
    занятию до 30/10/2021. Также не забывайте, что писать даты в заданиях нужно согласно
    установленного формата 11.01.1900
"""
# RE_DATE_3 = re.compile(r'(\d{2}[./-]){2}\d{4}')
RE_DATE_3 = re.compile(r'(\d{2}[./-]){2}\d{4}')  # TODO уточнение почему берет вторую часть, а не первую
print()
print(RE_DATE_3.findall(own_text))
print(RE_DATE_3.search(own_text))
print(RE_DATE_3.match(own_text))
print(*RE_DATE_3.finditer(own_text))

print()
RE_COST = re.compile(r'\d*\s*\d+[.,]\d+')
row_csv = "Стоимость данного товара составляет 10 001.50 рублей, а со скидкой Вы получите его за 999,99 рублей."
print(RE_COST.split(row_csv))
RE_COST_2 = re.compile(r'(\d*\s*\d+[.,]\d+)\s+(\b\w+\b)')
print(RE_COST.findall(row_csv))
print(RE_COST_2.findall(row_csv))


print()


# ДЕКОРАТОРЫ
import random
import json
import pickle
import os
from time import perf_counter

BASE_DIR = os.path.dirname(__file__)


def decorator_func(func):
    print('Я - декоратор')
    def wrapper(*args, **kwargs):
        print('Я - обёртка')

        start = perf_counter()
        result = func(*args, **kwargs)
        print(f'Время сохранения данных: {perf_counter() - start}')

        return result

    return wrapper


# @decorator_func
# def file_saver(future_name_file: str, numbers: list, databytes=False) -> str:
#     """Функция сохранения переданного списка в файл
#     :param future_name_file: название файла, который будет сохранён в директории trash
#     :param numbers: список элементов
#     :param databytes: флаг сохранения данных в байтах или строково
#     :return: str
#     """
#     # print('я file_saver')
#     dir_path = os.path.join(BASE_DIR, 'trash')
#     file_path = os.path.join(BASE_DIR, f'trash/{future_name_file}')
#     if not os.path.exists(dir_path):
#         os.mkdir(dir_path)
#
#     manager = (json, pickle)[databytes]
#     mode = 'wb' if databytes else 'w'
#     with open(file_path, mode) as fw:
#         manager.dump(numbers, fw)
#     return 'Я закончил'


nums = [random.random() * 10 ** 3 for _ in range(10 ** 6)]

# print(file_saver('json_saver.json', nums))
# print(file_saver('pickle_saver.pickle', nums, databytes=True))


# несколько декораторов и декоратор с аргументами
def print_docs(verbosity=0):
    print('АТРИБУТНАЯ ОБЁРТКА')
    def _logger(func):
        print('ДЕКОРАТОР')
        def wrapper(*args, **kwargs):
            print('ФУНКЦИОНАЛЬНАЯ ОБЁРТКА')
            msg = ''
            result = func(*args, **kwargs)
            if verbosity == 0:
                msg = f'\tcall {func.__name__} -> {result}'
            if verbosity > 0:
                msg = f'\tcall {func.__name__}\n{func.__doc__}\nРезультат: {result}'
            return msg

        return wrapper

    return _logger


@decorator_func
@print_docs(verbosity=0)
def file_saver(future_name_file: str, numbers: list, databytes=False):
    """Функция сохранения переданного списка в файл
    :param future_name_file: название файла, который будет сохранён в директории trash
    :param numbers: список элементов
    :param databytes: флаг сохранения данных в байтах или строково
    :return: None
    """
    print('Работник сохранения')
    dir_path = os.path.join(BASE_DIR, 'trash')
    file_path = os.path.join(BASE_DIR, f'trash/{future_name_file}')
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    manager = (json, pickle)[databytes]
    mode = 'wb' if databytes else 'w'
    with open(file_path, mode) as fw:
        manager.dump(numbers, fw)
    return 'Я закончил'


nums = [random.random() * 10 ** 3 for _ in range(10 ** 6)]

print()
print()
print(file_saver('json_saver.json', nums))

print()


print('end')
