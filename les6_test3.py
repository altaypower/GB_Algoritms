"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
 в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
 эффективным использованием памяти.
"""

"""
Найти простые числа до заданного числа N. Решето Эратосфена.
"""
import sys

print(sys.version, sys.platform)
n = 20

sieve=[i for i in range(n)]
sieve[1]=0
for i in range(2, n):
    if sieve[i] != 0:
        j = i*2
        while j < n:
            sieve[j] = 0
            j += i
result = [i for i in sieve if i != 0]
print(result)

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
print(f"Переменные в памяти занимают {summa} байт")