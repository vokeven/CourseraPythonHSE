def power(a, n):
    grd = 1
    if n > 0:
        while n > 0:
            grd *= a
            n -= 1
    elif n < 0:
        n = -n
        while n > 0:
            grd *= 1 / a
            n -= 1
    return grd

a = float(input())
n = int(input())
print(power(a, n))
