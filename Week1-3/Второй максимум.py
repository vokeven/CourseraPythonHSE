N1 = int(input())
N2 = int(input())
N = N2
maxLast = N1
maxSecond = N2
if N2 > N1:
    maxLast, maxSecond = N2, N1
while N != 0:
    N = int(input())
    if N >= maxSecond and N >= maxLast:
        maxSecond = maxLast
        maxLast = N
    elif N >= maxSecond and N <= maxLast:
        maxSecond = N
print(maxSecond)
