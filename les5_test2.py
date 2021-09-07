"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Использование встроенных функций для перевода из одной системы счисления
 в другую в данной задаче под запретом.
"""
from collections import deque, OrderedDict

class Hex_calc():
    def __init__(self):
        self.dict_hex = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
            'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
        # Создал упорядоченный словарь соответствия десятичных и шестнадцатеричных чисел
        self.dict_index = OrderedDict(self.dict_hex.items())

    def hex_to_dec(self, hex):
        # функция преобразует шестнадцатеричные числа в десятичные
       dec = 0
       for i in range(len(hex)):
          dec += int(self.dict_index[hex[i]]) * 16**i
       return dec

    def dec_to_hex(self, num):
        res = deque()
        list_index = list(self.dict_index.keys())
        while num != 0:
            # этот цикл преобразует десятичные числа в шестнадцатеричные
            res.appendleft(list_index[num % 16])
            num = num // 16
        return res

    def run(self):
        hex_1 = deque( input('Введите первое шестнадцатеричное число: ').upper())
        hex_2 = deque( input('Введите второе шестнадцатеричное число: ').upper())
        operand = input('Если хотите сложить числа, введите "+", если умножить введите "*": ')
        hex_1.reverse()
        hex_2.reverse()
        dec_1 = self.hex_to_dec(hex_1)
        dec_2 = self.hex_to_dec(hex_2)
        if operand == '+':
            res_dec = dec_1 + dec_2
        elif operand == '*':
            res_dec = dec_1 * dec_2
        #print(f"Результат: {''.join(res)}")
        print(f"Результат: {list(self.dec_to_hex(res_dec))}")

if __name__ == "__main__":
    Calculator = Hex_calc()
    Calculator.run()