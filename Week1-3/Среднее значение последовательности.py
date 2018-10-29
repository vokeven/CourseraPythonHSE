sumN = 0
i = 0
mid = 0
N = int(input())
while N != 0:
    sumN += N
    i += 1
    N = int(input())
mid = float(sumN) / i
print(mid)
