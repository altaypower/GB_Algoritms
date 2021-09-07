"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
 в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
 эффективным использованием памяти.
"""

"""
Найти простые числа до заданного числа N. Решето Эратосфена.
"""
import sys

print(sys.version, sys.platform) # 3.8.5 (default, Jan 27 2021, 15:41:15) [GCC 9.3.0] linux
n = 100

sieve={i: i for i in range(n)}
sieve[1]=0
for i in range(2, n):
    if sieve[i] != 0:
        j = i*2
        while j < n:
            sieve[j] = 0
            j += i
result = {i: sieve[i] for i in sieve if sieve[i] != 0}
print(list(result.keys()))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def var_size(x, level=0):
    size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += var_size(key, level + 1)
                size += var_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                size += var_size(item, level + 1)
    return size

summa = var_size(result) + var_size(sieve) + var_size(i) + var_size(j) + var_size(n)
print(f"Переменные в памяти занимают {summa} байт") # Переменные в памяти занимают 12652 байт


# Вывод: словари занимают памяти в несколько раз больше чем списки

