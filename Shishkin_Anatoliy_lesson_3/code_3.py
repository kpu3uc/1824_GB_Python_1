# Функции в Python

def func(a, b):
    """Пример простейшей функции"""
    c = a + b
    return c

a = 3
b = 5
value = func(a, b)
print(value)

value = func(3, 5)
print(value)
print(func(3, 5))

text_example_1 = 'Опыт выполнения домашних заданий предыдущих уроков наверняка подсказывает вам, ' \
                 'что нужен какой-то способ для повторного использования уже написанного кода.'
text_example_2 = 'Один из способов был изобретен очень давно — обособление фрагментов кода в функции. ' \
                 'Мы уже говорили о них.'

from Shishkin_Anatoliy_lesson_3.utils.string_transform import clear_punctuation, lower_and_split


for own_text in (text_example_1, text_example_2):
    new_text = clear_punctuation(own_text)
    print(lower_and_split(new_text))

# Возвращаем callback
# упрощённый пример
nums = ['1578.4', '892.4', '354.1', '871.5']
value = 0

for num in nums:
    value = value + float(num)

print(value)

# решение усложнённое
print(sum(map(float, nums)))

# docstring
# help(clear_punctuation)
# help(list)


# Области видимости переменных
def say_hello_wrapper():
    # name = 'Петр'

    def say_hello():
        print(name)

    say_hello()


name = 'Иван'
say_hello_wrapper()


# запрещённый проброс переменной из локальной области в глобальную
def say_hello():
    global name
    name = 'Петр'
    print(name)


name = 'Иван'
print(name)  # Иван
say_hello()  # Петр
print(name)


# ещё пример использования nonlocal
def wrapper():
    name = 'Анатолий'

    def say_hello():
        nonlocal name
        name = name[:-1]
        return name

    return say_hello


name = 'Иван'
callback = wrapper()
print(callback())
print(callback())
print(callback())
print(callback())



print()
# Словари Python (Ассоциативные массивы)
pers_1 = ['pikachu', 87.9, 103]
pers_2 = ['smurfik', 10.0, 66]


def get_info(data):
    print(f'Никнейм - {data[0]}, health - {data[1]}, level - {data[2]}')


get_info(pers_1)
get_info(pers_2)
print()


# upgrade pers
pers_1_adv = {
    "nickname": 'pikachu',
    "health": 87.9,
    "level": 103
}
pers_2_adv = {
    "nickname": 'smurfik',
    "health": 10.0,
    "level": 66
}


def get_info(dataset: dict) -> str:
    print(f'Никнейм - {dataset["nickname"]}, health - {dataset["health"]}, level - {dataset["level"]}')


get_info(pers_1_adv)
get_info(pers_2_adv)
print()


# Словари: .get() и .setdefault()
print(pers_1_adv.get('sex'))
print(pers_1_adv.get('sex', 'средний'))
print(pers_1_adv)
print()

print(pers_1_adv.setdefault('sex', 'man'))
print(pers_1_adv)
print(pers_1_adv.setdefault('nickname', 'Анатолий'))
print(pers_1_adv)
print()


# Словари: .update() и .popitem()
print(pers_1_adv.popitem())
print(dir(dict))
print(pers_1_adv.pop('level'))
print()


# Словари: цикл for in
dataset = {
    'mail.ru': '94.100.180.201',
    'geekbrains.ru': '178.248.232.209',
    'amazon.com': '205.251.242.103'
}

for man in dataset:
    print(man)

print()

for key in dataset.keys():
    print(key)

print()

for key, value in dataset.items():
    print('{}={}'.format(key, value))


# Позиционные аргументы и *args
from Shishkin_Anatoliy_lesson_3.utils.tools import own_sum, own_sum_upgrade

print(f'own_sum([1, 5, 89]) = {own_sum([1, 5, 89])}')
# print(own_sum(1, 5, 89)) # ОШИБКА
print(f'own_sum_upgrade(1, 5, 89) = {own_sum_upgrade(1, 5, 89)}') # НЕТ ОШИБКИ - WHY?
print(own_sum([1, 5, 89]) == own_sum_upgrade(1, 5, 89))


# разбираем распаковку
a = 5
b = 10
(a, b) = (b, a)

own_list = [1, 5, 89]
print(f'own_sum_upgrade(*[1, 5, 89]) = {own_sum_upgrade(*[1, 5, 89])}')
print(f'own_sum_upgrade(*own_list) = {own_sum_upgrade(*own_list)}')
print()



# Модуль random
from random import randrange, randint, choice

numbers = [value * 11 for value in range(1, 11)]
print(f'numbers = {numbers}')
print()
idx = randrange(len(numbers))  # как пользоваться randrange
print(f'idx = {idx}')
print(f'numbers[{idx}] = {numbers[idx]}')
print()
new_idx = randint(0, len(numbers) - 1)  # как пользоваться randint
print(f'new_idx = {new_idx}')
print(f'numbers[{new_idx}] = {numbers[new_idx]}')
print()
print(f'Случайное значение из списка {numbers} получили {choice(numbers)}')
print()
# choices, sample и shuffle - разбираем самостоятельно в методичке есть ссылки


# Необязательные аргументы, именованные аргументы - **kwargs
def my_game(count_game: int) -> None:
    """Играем на стандартном кубике"""
    for step in range(count_game):
        print(f'При броске на кубике выпало: {randint(1, 6)}')


my_game(2)
print()


def my_game(count_game: int, luck: float = 0.00) -> None:
    """Играем на стандартном кубике с удачей"""
    if luck > 100:
        luck = 100.00
    end_number = 6
    start_number = 1 + int(((end_number - 1) * luck) / 100)
    for step in range(count_game):
        print(f'При броске на кубике выпало: {randint(start_number, end_number)}')


my_game(2)
# print()
my_game(2, 100.00)
print()


def my_game(count_game: int, luck: float = 0.00, **kwargs) -> None:
    """Играем на кубике"""
    print(f'kwargs: {kwargs}')
    if luck > 100:
        luck = 100.00
    # end_number = 6
    end_number = kwargs.get('count_edge', 6)
    start_number = 1 + int((end_number - 1) * luck / 100)
    for step in range(count_game):
        print(f'При броске на кубике выпало: {randint(start_number, end_number)}')


my_game(2)
print()
my_game(2, luck=50)
print()
my_game(2, luck=50, count_edge=12, mars='asdfg', snikers=123.75)
print()



# где может понадобиться распаковка словаря
dataset_1 = {'name': 'Сергей', 'age': 106, 'sex': 'm'}
dataset_2 = {'health': 'small', 'luck': 0.5}



user_dataset = dict(
    **dataset_1, **dataset_2
)
print(user_dataset)
print()


# filter(), map(), zip() и lambda-функции
new_numbers = [value * 11 for value in range(20)]
print(f'new_numbers = {new_numbers}')
print()


def my_filter(element) -> bool:
    """Наша функция для фильтрации"""
    return element % 10 == 5


own_filter_result = filter(my_filter, new_numbers)
print(type(own_filter_result))
print('result =', *own_filter_result)
print('result =', *own_filter_result)  # а здесь уже ничего НЕ УВИДИМ кроме 'result ='
print()

own_filter_result = filter(lambda obj: obj % 10 == 5, new_numbers)
print('lambda filter result =', *own_filter_result)
print()

map_result = map(float, new_numbers)
print('map_result =', list(map_result))
print()

user_names = ['Иван', 'Петр', 'Ольга', 'Сергей']
user_logins = ['ivan', '', 'petr', 'olga']
user_roles = ['user', 'staff', 'admin', 'user']
zip_result = zip(user_names, user_logins, user_roles)
for name, login, role in zip_result:
    print(f'{name} - {login} - {role}')

print('zip_result =', tuple(zip_result))
print()


print('end')