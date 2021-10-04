# что такое типы и как их проверять
a = 1
print(type(a))

if not isinstance(a, int):
    print('Я Integer')

print(type(a) == bool)

# Как смотреть методы объекта
im_list = list()
print(dir(im_list))

# Методы списка
im_list.append(100)
print(f'{im_list} - {len(im_list)}')

im_list.extend([10, 'Сергей'])
print(f'{im_list} - {len(im_list)}')

im_list.append(['Евлампий', 15])
print(f'{im_list} - {len(im_list)}')

im_list.extend([10, 15])
print(f'{im_list} - {len(im_list)}')


search_value = 10
print('Количество искомого', 10, '-', im_list.count(search_value))


year = ['январь', 'февраль', 'март', 'апрель', 'май']
print(year)
element_1 = year.pop()
print(element_1)
print(year)

element_2 = year.pop(2)
print(element_2)
print(year)

print(year.index('январь'))
# print(year.index('декабрь'))

year.insert(2, 'март')
year[3] = 'super'
print(year)

year.append('март')
print(year)

while year.count('март'):
    year.remove('март')

print(year)


# Реверсы и срезы списков
# параметры среза obj[start=0, stop=len(obj), step=1]
print('Реверс списка in_place')
print(id(year), year)
year.reverse()
print(id(year), year)

print('Реверс списка not in_place')
print(id(year), year)
year_reversed = list(reversed(year))
print(id(year_reversed), year_reversed)

print('Ещё один способ реверса')
print(id(year), year)
new_year = year[::-1]
print(id(new_year), new_year)

print('Hello world!'[6:-1])
year = year[::-1]
# Сортировки списков
# print('Сортировка in_place')
# print(id(year), year)
# year.sort()
# # year.sort(reverse=True)
# print(id(year), year)

print('Сортировка not in_place')
print(id(year), year)
year_sorted = sorted(year)
# year_sorted = sorted(year, reverse=True)
print(id(year_sorted), year_sorted)

# Кортежи
import sys
from os import path

some_list = ['hello', True, 'word', 1, 2.2]
print(type(some_list), sys.getsizeof(some_list), some_list)
some_tuple = ('hello', True, 'word', 1, 2.2)
print(type(some_tuple), sys.getsizeof(some_tuple), some_tuple)

print(year)
print(set((*year, 'январь', 'январь', 'февраль')))

a = [['hello'], 10]
b = a
print(id(a), id(b))
b[1] = 15
print(a, b)
print(id(a), id(b))

from copy import copy, deepcopy

a = [['hello'], 10]
b = a.copy()
print(id(a), id(b))
b[1] = 15
b[0].append('world')
print(a, b)
print(id(a), id(b))

a = [['hello'], 10]
b = deepcopy(a)
print(id(a), id(b))
b[1] = 15
b[0].append('world')
print(a, b)
print(id(a), id(b))

# Работа со строками
hello = list('Hello world!')
print(hello)

print(f'я - {ord("я")}')
print(f'{chr(ord("я") - 32)} - {ord(chr(ord("я") - 32))}')


# Строки
print('Форматирование строк')
name = 'Анатолий'
minute = 5
print('Проснись, %s! Вебинар скоро закончится. Осталось %d минут.' % (name, minute))
print('Проснись, {:^20}! Вебинар скоро закончится. Осталось {:.2f} минут.'.format(name, minute))
print(f'Проснись, {name:^20}! Вебинар скоро закончится. Осталось {minute:.2f} минут.')

# split(), параллельное присваивание с распаковкой
# join()
# upper() и lower()
# title() и capitalize()

print('Конкатенация')
print('С' + 'новым' + 'годом' + '!')
ll = ['С', 'новым', 'годом', '!']
print(' '.join(ll))

print('С новым годом !'.split())
print('С новым годом !'.split('о'))


# ascii

message = 'екшамод к ьрепет илангоп'
print(message[::-1])


print('end')


