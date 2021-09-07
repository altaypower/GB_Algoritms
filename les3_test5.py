"""
 В массиве найти максимальный отрицательный элемент.
 Вывести на экран его значение и позицию в массиве.
"""

import random

def max_negative_el(lst):
    big = -1000
    idx = 100
    for i in range(len(objct)):
        if objct[i] < 0:
            if objct[i] > big:
                big = objct[i]
                idx = i
    if big == -1000:
        #Почти невозможный случай, но все же
        print('Отрицательных чисел в массиве нет')
    else:
        print(f"Максимальный отрицательный элемент массива {objct} равен {big} и его позиция в массиве{idx+1}")

objct = [random.randint(-6, 3) for i in range(10)]
max_negative_el(objct)