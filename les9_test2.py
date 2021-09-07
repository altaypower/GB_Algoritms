
#Закодируйте любую строку по алгоритму Хаффмана.

import collections


count_dict = collections.Counter()
#entry_str = "beep boop beer!"
entry_str = input("Введите строку для кодирования: ")
entry_list = list(entry_str)
for word in entry_list:
    count_dict[word] += 1

while len(count_dict) != 1: # цикл работает пока все буквы не придут в одну строку
    count_dict = collections.OrderedDict(sorted(count_dict.items(), key=lambda t: t[1]))
    first = count_dict.popitem(last = False) # извлекаю из коллекции первый отсортированный элемент
    second = count_dict.popitem(last = False) # извлекаю из коллекции второй отсортированный элемент

    first = list(first) # преобразую буквы первого элемента, добавояя перед ними требуемый шифр
    first[0] = first[0].split(',')
    e = ['0' + i for i in first[0]]
    str_first = e[0]
    for j in range(1, len(e)):
        str_first += ',' + e[j]

    second = list(second) # преобразую буквы второго элемента, добавояя перед ними требуемый шифр
    second[0] = second[0].split(',')
    d = ['1' + i for i in second[0]]
    str_second = d[0]
    for j in range(1, len(d)):
        str_second += ',' + d[j]

    count_dict[str_first + ',' + str_second] = first[1] + second[1] # добавил собранный элемент в конец коллекции
    count_dict.move_to_end(str_first + ',' + str_second, last=False) # перенес собранный элемент в начало коллекции, чтобы он
    # отсортировался перед другими элементами с таким же весом

count_list = list(count_dict) # извелаю из коллекции список символов с кодом
coder_list = count_list[0].split(',')

coder_dict = dict() # создаю словарь для кодировки
for value in coder_list:
    coder_dict[value[-1]] = value[: -1]

res = '' # получаю закодированную строку
for i in entry_list:
    res += coder_dict[i] + ' '
print(res)


