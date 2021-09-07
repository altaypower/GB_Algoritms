"""
 Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции
 дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля
hashlib задача считается не решённой.
"""
import hashlib

def substr_find(s:str):
    assert len(s) > 0, 'Строки не могут быть пустыми'
    my_dict = {}

    len_s = len(s)
    for i in range(1, len_s):
        for j in range(len_s - i + 1):
            cnt = 0
            substr = s[j:j+i]
            h_substr = hashlib.sha1(substr.encode('utf-8')).hexdigest()
            for _ in range(len_s - len(substr) +1):
                if h_substr == hashlib.sha1(s[_:_ + len(substr)].encode('utf-8')).hexdigest():
                    cnt += 1
            my_dict[substr] = cnt
    for key in my_dict.keys():
        print(f"Подстрока {key} в строке {s} встречается {my_dict[key]} раз(а)")

s = input('Введите строку: ')


pos = substr_find(s)


