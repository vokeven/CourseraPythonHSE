n = int(input())
maxN = 0
i = 1
while n != 0:
    n2 = int(input())
    if n2 == n:
        i += 1
    else:
        if i > maxN:
            maxN = i
        i = 1
    n = n2
print(maxN)
