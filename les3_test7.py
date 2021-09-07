"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

from random import randint

def two_min(lst):
    min_el_1 = 0
    min_el_2 = 0
    j = 1
    for el in lst:
        if j == 1:
            min_el_1 = el
            min_el_2 = el
            j += 1
        elif el < min_el_1:
            min_el_1 = el
    lst.remove(min_el_1)
    """
    Находим первый минимальный элемент и удаляем его из списка,
    затем еще один цикл для поиска второго минимального элемента.
    """
    for el in lst:
        if (el < min_el_2) and (el >= min_el_1):
            min_el_2 = el
    return f'Первый наименьший элемент: {min_el_1}\n' \
           f'Второй наименьший элемент: {min_el_2}'


random_list = [randint(1, 100) for _ in range(0, 20)]
print(f'Исходный список:\n{random_list}\n')
print(two_min(random_list))