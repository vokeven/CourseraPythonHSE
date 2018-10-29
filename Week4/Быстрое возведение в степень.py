def power(a, n):
    if n > 0:
        if n % 2 == 0:
            return power(a ** 2, n / 2)
        else:
            return a * power(a ** 2, (n - 1) / 2)
    elif n < 0:
        n = -n
        if n % 2 == 0:
            return 1 / power(a ** 2, n / 2)
        else:
            return 1 / (a * power(a ** 2, (n - 1) / 2))
    else:
        return 1


a = float(input())
b = int(input())
print(power(a, b))
