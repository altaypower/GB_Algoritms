"""
Найти наибольший общий делитель (НОД, greatest
common divisor, gcd) пары чисел c помощью алгоритма Евклида.
"""

def gcd(m, n):
    if n==0:
        return m
    return gcd(n, m % n)

print(gcd(24, 562))

def gcd_cycle(m, n):
    while n != 0:
        m, n = n, m % n
    return m

print(gcd_cycle(25, 125))