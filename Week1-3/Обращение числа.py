N = int(input())
res = 0
while N != 0:
    res = N % 10
    N = (N - res) // 10
    print(res, end='')
