def ReduceFraction(n, m):
    if m != 0:
        return ReduceFraction(m, n % m)
    return (a // n, b // n)

a = int(input())
b = int(input())

print(ReduceFraction(a, b)[0], ReduceFraction(a, b)[1])
