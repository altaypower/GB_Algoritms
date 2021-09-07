"""
В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы.
"""
import random

def change_min_max(lst):
    print(lst)
    # ищу индекс и значение минимального и максимального элементов
    small = [0, 100]
    big = [0, 0]
    for i, item in enumerate(lst):
        if item < small[1]:
            small = [i, item]
        elif item > big[1]:
            big = [i, item]
    # и меняю их местами
    lst[small[0]], lst[big[0]] = big[1], small[1]
    print(lst)

random_list = [random.randint(1, 100) for i in range(10)]
change_min_max(random_list)

