def phib(n):
    if n > 2:
        return phib(n - 2) + phib(n - 1)
    if n == 1 or n == 2:
        return 1
    else:
        return 0


n = int(input())
print(phib(n))
