"""
Сформировать из введенного числа обратное по порядку
входящих в него цифр и вывести на экран. Например, если
введено число 3486, то надо вывести 6843.
"""

def inversion(num, n):
    if n==1:
        return f"{num[n-1]}"
    elif n>1:
        return f"{num[n-1]}{inversion(num, n-1)}"

try:
    num = int(input("Введите число для реверса: "))
    n=len(num)
    print(inversion(num, n))
except ValueError:
    print('Ошибка! Введено неверное значение!')
