N = int(input())
maxLast = N
i = 1
while N != 0:
    N2 = int(input())
    if N2 > maxLast:
        maxLast = N2
        i = 1
    elif N2 == maxLast:
        i += 1
    N = N2
print(i)
