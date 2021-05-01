"""
Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ"""

import random

print('Введите два целых числа')
a = int(input('a = '))
b = int(input('b = '))
n = random.randint(a, b)
print(n)

print('Введите два целых числа')
a = int(input('a = '))
b = int(input('b = '))
rand=random.Random()
n = a+rand.random()*(b-a)
print(round(n, 3))

print('Введите два символа')
a = ord(input('a = '))
b = ord(input('b = '))
n = int(rand.random() * (b-a+1)) + a
print(chr(n))

