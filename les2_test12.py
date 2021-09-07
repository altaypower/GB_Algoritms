"""
Написать программу, доказывающую или проверяющую, что для
множества натуральных чисел выполняется равенство:
1 + 2 + ... + n = n × (n + 1) / 2,
где n – любое натуральное число.
"""
from random import randrange

n = randrange(100)
sum = 0
for i in range(n+1):
    sum += i
if sum == n *(n + 1) / 2:
    print("Равенство доказано")

for i in [item for item in dir() if not item.startswith("__")]:
     print(i)

"""
# рекурсия

def sumn(n, s=0):
    if n == 0:
        return s
    else:
        s += n
        return sumn(n - 1, s)

# проверяем утверждение
def check(n):
    if sumn(n) == n * (n + 1) / 2:
        return True
    else:
        return False

num = int(input('Введите число n: '))
print(check(num))
"""