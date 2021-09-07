"""
Проанализировать скорость и сложность одного любого алгоритма
    из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом
    (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
"""
# python --version 3.9.0
from timeit import timeit
from cProfile import run
from random import randint

"""
Задача 2 из урока 3, в которой было необходимо во втором массиве сохранить
индексы четных элементов первого массива. 
"""


# первый вариант через цикл for in
def even_index(arr):
    """
    Функция принимает в себя список чисел,
    индексы четных элементов которого будем
    помещать в новый список arr_index
    """
    arr_index = []
    for i, el in enumerate(arr):
        """
        Используем функцию enumerate(), которая 
        возвращает кортеж (индекс елемента, сам элемент).
        если элеммент el четный, то его индекс i
        помещаем в списко arr_index
        """
        if el % 2 == 0:
            arr_index.append(i)
    return arr_index


# Второй вариант через генераторное выражение
def even_index_gen(arr):
    arr_index = [i for i, j in enumerate(arr) if j % 2 == 0]
    return arr_index


# Третий вариант через рекурсию
def even_index_vr2(arr, arr_index=[], i=0):
    if i == len(arr):
        return arr_index
    else:
        if arr[i] % 2 == 0:
            arr_index.append(i)
            even_index_vr2(arr, arr_index, i + 1)
        else:
            even_index_vr2(arr, arr_index, i + 1)
    return arr_index


# Четвертый вариант через цикл while
def even_index_vr3(arr):
    i = 0
    arr_index = []
    while i < len(arr):
        if arr[i] % 2 == 0:
            arr_index.append(i)
        i += 1
    return arr_index


even_arr_10 = [randint(1, 100) for el in range(0, 10)]
even_arr_100 = [randint(1, 100) for el in range(0, 100)]
even_arr_1000 = [randint(1, 100) for el in range(0, 1000)]
even_arr_10000 = [randint(1, 100) for el in range(0, 10000)]
# покажем, что все четыре варианта работают
print(f'Исходный список:\n{even_arr_10}\n\n'
      f'Вариант первый через for in:\n{even_index(even_arr_10)}\n\n'
      f'Вариант второй через генераторное выражение:\n{even_index_gen(even_arr_10)}\n\n'
      f'Вариант третий через рекурсию:\n{even_index_vr2(even_arr_10)}\n\n'
      f'Вариант четвертый через while:\n{even_index_vr3(even_arr_10)}\n\n')

"""
Результат:

Исходный список:
[35, 14, 16, 30, 42, 31, 90, 96, 52, 66]

Вариант первый через for in:
[1, 2, 3, 4, 6, 7, 8, 9]

Вариант второй через генераторное выражение:
[1, 2, 3, 4, 6, 7, 8, 9]

Вариант третий через рекурсию:
[1, 2, 3, 4, 6, 7, 8, 9]

Вариант четвертый через while:
[1, 2, 3, 4, 6, 7, 8, 9]

Process finished with exit code 0

Все функции работают верно!!! Анализируем их через timeit и cProfile
"""

# сначала анализируем через timeit
# анализируем первый вариант for in на разных по количеству элементов списках
print(
    timeit(
        "even_index(even_arr_10)",
        setup="from __main__ import even_index, even_arr_10",
        number=1000
    )
)

print(
    timeit(
        "even_index(even_arr_100)",
        setup="from __main__ import even_index, even_arr_100",
        number=1000
    )
)

print(
    timeit(
        "even_index(even_arr_1000)",
        setup="from __main__ import even_index, even_arr_1000",
        number=1000
    )
)

print(
    timeit(
        "even_index(even_arr_10000)",
        setup="from __main__ import even_index, even_arr_10000",
        number=1000
    )
)

"""
Результат:
список из 10 элементов - 0.0011494999999999977
список из 100 элементов - 0.008471100000000002
список из 1000 элементов - 0.08517910000000001
список из 10000 элементов - 0.8201016
Вывод: при увеличении списка в 10 раз время увеличивается в 10 раз
"""

# анализируем вторй вариант с генераторным выражением
print()
print(
    timeit(
        "even_index_gen(even_arr_10)",
        setup="from __main__ import even_index_gen, even_arr_10",
        number=1000
    )
)

print(
    timeit(
        "even_index_gen(even_arr_100)",
        setup="from __main__ import even_index_gen, even_arr_100",
        number=1000
    )
)

print(
    timeit(
        "even_index_gen(even_arr_1000)",
        setup="from __main__ import even_index_gen, even_arr_1000",
        number=1000
    )
)

print(
    timeit(
        "even_index_gen(even_arr_10000)",
        setup="from __main__ import even_index_gen, even_arr_10000",
        number=1000
    )
)
"""
Результат:
список из 10 элементов - 0.0009523999999999644
список из 100 элементов - 0.006139100000000064
список из 1000 элементов - 0.07639590000000007
список из 10000 элементов - 0.7188428
Вывод: быстрее чем первый вариант. Время также растет пропорционально величене списка.
"""
# анализируем третий варент, рекурсию
print()
print(
    timeit(
        "even_index_vr2(even_arr_10)",
        setup="from __main__ import even_index_vr2, even_arr_10",
        number=1000
    )
)

print(
    timeit(
        "even_index_vr2(even_arr_100)",
        setup="from __main__ import even_index_vr2, even_arr_100",
        number=1000
    )
)
"""
Результат:
список из 10 элементов - 0.002585099999999896
список из 100 элементов - 0.02499539999999989
список из 1000 элементов и 10000 не рассматриваем, т.к. переполнение стека вызова рекурсии
Вывод: работает медленнее чем for in и генератор списка.
"""
# анализируем четвертый вариант while:
print()
print(
    timeit(
        "even_index(even_arr_10)",
        setup="from __main__ import even_index, even_arr_10",
        number=1000
    )
)

print(
    timeit(
        "even_index(even_arr_100)",
        setup="from __main__ import even_index, even_arr_100",
        number=1000
    )
)

print(
    timeit(
        "even_index(even_arr_1000)",
        setup="from __main__ import even_index, even_arr_1000",
        number=1000
    )
)

print(
    timeit(
        "even_index(even_arr_10000)",
        setup="from __main__ import even_index, even_arr_10000",
        number=1000
    )
)
"""
Результат:
список из 10 элементов - 0.0008989999999999831
список из 100 элементов - 0.007251399999999908
список из 1000 элементов - 0.0828833
список из 10000 элементов - 0.8077372999999999
Вывод: Работает примерно также как и for in

Общий вывод по timeit генераторное выражение самы оптимальный вариант из преддложенных
"""


# анализ через cProfile
# для краткости объединим все варианты в одну функцию
def analyse_func():
    res_1 = even_index(even_arr_100)
    res_2 = even_index_gen(even_arr_100)
    res_3 = even_index_vr2(even_arr_100)
    res_4 = even_index_vr3(even_arr_100)


run('analyse_func()')
"""
Результат:

         461 function calls (361 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task1.py:26(even_index)
        1    0.000    0.000    0.000    0.000 task1.py:264(analyse_func)
        1    0.000    0.000    0.000    0.000 task1.py:46(even_index_gen)
        1    0.000    0.000    0.000    0.000 task1.py:47(<listcomp>)
    101/1    0.000    0.000    0.000    0.000 task1.py:52(even_index_vr2)
        1    0.000    0.000    0.000    0.000 task1.py:65(even_index_vr3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      202    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      150    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
        
        
 Process finished with exit code 0"""
