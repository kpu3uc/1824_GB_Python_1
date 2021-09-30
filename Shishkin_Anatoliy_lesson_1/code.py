# print(int(5.87))
# print(float(5.87))
# True
# False
# print(bool(1))
# print(bool(0))
# print(bool(''))
# print(bool('Я текст'))
# print(type(5))
# print(type(5.55))
# print(type('5'))
# print(type(True))
# a = 100
# b = 5.5
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# Я комментарий

"""
Логические операции Напоминаем, что для сравнения вы используете:
a = 100
b = 5.5
a > b                = True
a < b                = False
a == b               = False
a != b               = True
a >= b               = True
a <= b               = False
bool(a and b)        = True
bool(a and None)     = False
bool(a or b)         = True
bool(not a or b)     = True
bool(not a or not b) = False
a in [1, 2, 3]       = False
a not in [1, 2, 3]   = True
a is 100             = True
a is not 100         = False
100 is a             = True
instance = int(5)    = 5
instance == 5        = True
instance is 5        = True
instance is int()    = False
instance is int      = False
instance is instance = True
"""
# hello = 'привет'
hello = None
# ctrl + /
# if hello:
#     print(hello)
# if hello != 'sdf':
#     print(hello)
# else:
#     print('stop')

# if not hello:
#     print(hello)
# elif hello != 'sdf':
#     print(hello)
# else:
#     print('stop')

# print('end')

a = 10
# while a > 0:
#     print(a)
#     a -= 1 # a = a - 1
#     # a += 1

# while True:
#     # тело цикла
#     if a >= 15:
#         # тело ветвления
#         break
#     print(a)
#     a += 1
#     # окончание тела цикла


# for x in [10, 25, 3]:
#     print(x)

# range
# for x in range(6, 1, -1):
#     print(x)
#
# print('end')
#
# print(len([10, 25, 3]))

for index, key in enumerate(['a', 'b', 'c'], start=1):
    print(f'{index} - {key}')

