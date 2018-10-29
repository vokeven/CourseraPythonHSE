import math


def cube(n, k):
    n1 = math.ceil(n ** (1/3))
    # База рекурсии: число и есть квадрат
    if n1 ** 3 == n:
        print(n1 ** 3, end='')
        return int(n1 ** 3)
    # Иначе придется перебирать от n1 до 1 вниз
    while n1 >= 1:
        s = n1 ** 3
        # Если еще укладываемся в 7 чисел
        if k <= 6:
            s += cube(n - n1 ** 3, k + 1)
        # Нашли сумму квадратов. Выводим через пробел, не перенося строку
        if s == n:
            print(' ', n1 ** 3, sep='', end='')
            return int(s)
        elif k == 1 and n1 == 1:
            print(0)
        n1 -= 1
    return 0


n = int(input())
cube(n, 1)
