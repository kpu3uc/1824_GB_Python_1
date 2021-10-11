# Батарейки для Python: pypi.org

from num2words import num2words

print(num2words(42))
print(num2words(42, to='ordinal'))
print(num2words(42, to='ordinal_num'))
print(num2words(42, to='year'))
print(num2words(12.42, to='currency'))
print(num2words(42, lang='ru'))

# https://github.com/sivel/speedtest-cli

# Установим пару библиотек — requests и pillow:

# Модули и пакеты в Python
# hello_module.py
from hello import hello_module
from hello.hello_module import say_hello, hello2
from hello.hello_module import say_hello as sh



hello_module.say_hello('Сергей')
say_hello('Роман')
sh('Владислав')

# hello_module


# Рекомендуем в будущем изучить модуль argsparse — он позволяет писать серьёзные инструменты для командной строки.
# argsparse - https://docs.python.org/3.8/library/argparse.html#module-argparse

# Модуль time: профилируем время выполнения участков кода
# time_profiler.py

# Модуль datetime: работа с датой и временем
# datetime_difference.py


from cbr_parser.utils import extract_data


print(extract_data('Name'))



print('end')