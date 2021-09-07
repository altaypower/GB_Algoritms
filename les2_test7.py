"""
Посчитать четные и нечетные цифры введенного натурального
числа. Например, если введено число 34560, то у него 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

def even_odd_numbers(n): # тут все понятно без слов

    even_numbers = 0
    odd_numbers = 0
    for i in range(len(n)):
        if int(n[i])%2==0:
            even_numbers += 1
        else:
            odd_numbers += 1
    print(f"Количество четных цифр: {even_numbers},количество нечетных: {odd_numbers}")

try:
    n = input("Введите целое число: ")
    even_odd_numbers(n)
except ValueError:
    print('Ошибка! Введено неверное значение!')

"""
Решение через рекурсию:

def even_odd(num, even_num=0, odd_num=0):
    # указываю базовый случай
    if num == 0:
        return f'Количество четных цифр: {even_num},\n' \
               f'Количество нечетных цифр: {odd_num}.'

    # Если условия для завершения рекурсии не выполнены
    else:
        # Проверяем четность чила и отщипываем последнюю цифру
        if num % 2 == 0:
            # Если четное, то увеличиваем even_num
            return even_odd(num // 10, even_num + 1, odd_num)
        else:
            # Если нечетное, то увеличиваем odd_num
            return even_odd(num // 10, even_num, odd_num + 1)

try:
    nums = int(input('Введите число: '))
    print(even_odd(nums))
except ValueError:
    print('Ошибка! Введено неверное значение!')
"""