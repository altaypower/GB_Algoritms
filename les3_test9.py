"""
Урок 3. Задача 9.
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
# python --version 3.9.0
from random import randint


def matrix_method(mtrx):
    min_elms_matrix = []
    max_el = -1
    for i in range(len(mtrx[0])):
        min_el = 0
        j = 1
        for el in mtrx:
            if j == 1:
                min_el = el[i]
                j += 1
            elif el[i] < min_el:
                min_el = el[i]
        min_elms_matrix.append(min_el)
        if min_el > max_el:
            max_el = min_el
    return f'Список минимальных элемнтов столбцов матрицы:\n{min_elms_matrix}\n' \
           f'\nМаксимальное число среди этих элементов равно {max_el}'


matrix = [[randint(1, 99) for _ in range(10)] for _ in range(5)]
"""
выведем матрицу на экран
"""
for line in matrix:
    for i in line:
        print(f'{i:>4}', end='')
    print()

print()
print(matrix_method(matrix))