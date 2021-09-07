"""
Определить, какое число в массиве встречается чаще всего
"""

import random


def frequent_el(lst):
    num = set(lst)
    num = list(num)
    res = [0] * len(num)
    for i, item in enumerate(num):
        for j in lst:
            if item == j:
                res[i] += 1

    big = 0
    for _ in res:
        if _ > big:
            big = _
    for x, itm in enumerate(res):
        if itm == big:
            print(f"Наибольшее (одно из наибольших) число вхождений в массив {lst} у числа {num[x]}")

random_list = [random.randint(1, 4) for i in range(10)]
frequent_el(random_list)

"""
# другой вариант, через функцию

from random import randint

def num_counter(arr):
    num = arr[0]
    cnt = 1
    for i in range(len(arr) - 1):
        n = 1
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                n += 1
        if n > cnt:
            cnt = n
            num = arr[i]

    print(f'Чаще всего встречается число {num},\n'
          f'оно встречается {cnt} раз(а)')

s = '-'
random_list = [randint(1, 10) for i in range(0, 20)]
print(random_list)
num_counter(random_list)
"""