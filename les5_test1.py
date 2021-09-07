"""
Пользователь вводит данные о количестве предприятий,
    их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""
# python --version 3.9.0
from collections import Counter



class StatisticsFirms:
    def __init__(self):
        self.profit_lst = []  # Список годовой прибыли для каждой фирмы
        self.firm_dict = {}  # Словарь {название: прибыль за год}
        self.below_average = []  # Список фирм с прибылью ниже средней
        self.above_average = []  # Список фирм с прибылью выше средней

    def firms_and_profit(self):  # I Введение данных от пользователя
        ex = 'yes'
        while ex == 'yes':
            """
            Пользователь вводит запрашиваемые программой данные о предприятиях,
            до тех пор пока не введет необходимое значение для выхода в конце цикла
            """
            company = input('Введите название предприятия:\n')
            profit = input('Через пробел введите прибыль данного предприятия'
                           'за кажджый квартал(Всего 4 квартала):\n').split(' ')
            if sum(Counter(profit).values()) != 4:  # проверяем, что у нас 4е элемента
                print('Необходимо ввести 4 числа через пробел, попробуйте еще раз')
                continue
            else:
                try:  # приводим все элементы profit к int
                    profit = list(map(int, profit))
                except ValueError:
                    print('Необходимо ввести 4 числа через пробел, попробуйте еще раз')
                    continue
                self.profit_lst.append(sum(profit))
                self.firm_dict[company] = sum(profit)
                ex = input('Желаете продолжить? '
                           'Тогда наберите слово yes, для завершения нажмите любую клавишу:\n').lower()
        return self.firm_dict and self.profit_lst

    def analysis_firms(self):
        """
        определяем среднюю годовую прибыль и находим фирмы с доходом выше и ниже среднего
        """
        middle_year_profit = sum(self.profit_lst)/sum(Counter(self.profit_lst).values())  # II
        for key, value in self.firm_dict.items():
            if value < middle_year_profit:
                self.below_average.append(key)  # IV
            elif value > middle_year_profit:
                self.above_average.append(key)  # III
        return f'Средняя годовая прибыль по указанным предприятиям: {middle_year_profit}\n' \
               f'Предприятия с прибылью выше среднего: {self.above_average}\n' \
               f'Предприятия с прибылью ниже среднего: {self.below_average}.'


stat_firms1 = StatisticsFirms()
stat_firms1.firms_and_profit()
print(stat_firms1.analysis_firms())
