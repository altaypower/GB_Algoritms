"""
Даны 2 целых числа. Необходимо вывести все числа от А до В включительно в порядке возрастания,
если А < В и в порядке убывания, если А > B.
"""

def func(a, b):
    if a==b:
        return f"{a}"
    elif a>b:
        return f"{a}, {func(a-1, b)}"
    elif a<b:
        return f"{a}, {func(a+1, b)}"

print(func(1, 10))

def func_cycle(a, b):
    if a==b:
        return f"{a}"
    elif a > b:
        while a!=b:
            print(a)
            a-=1
        print(a)
    elif a < b:
        while a!=b:
            print(a)
            a+=1
        print(a)

func_cycle(1, 10)


