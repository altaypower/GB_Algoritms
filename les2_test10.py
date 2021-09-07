"""
Вывести на экран коды и символы таблицы ASCII, начиная с
символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар «код-
символ» в каждой строке.
"""

for i in range(32,128):
    print(f"{i}-{chr(i)}", end='  ')
    if i%10==1: # переход на новую строку
        print()

"""
рекурсия
def cod(first_symbol, last_symbol, step=1):
    # базовое условие - первый символ на 1 больше последнего
    if first_symbol == last_symbol + 1:
        return ''
    else:
        #Если шаг кратен десяти, тогда в конце строки ставим '\n',
        #если не кратен, тогда в конце строки ставим пробел,
        #таким образом выводим по десять пар в строке
        if step % 10 != 0:
            print(f'{first_symbol} - {chr(first_symbol)}', end=' ')
        else:
            print(f'{first_symbol} - {chr(first_symbol)}', end='\n')
        return cod(first_symbol + 1, last_symbol, step + 1)


cod(32, 127)
"""





