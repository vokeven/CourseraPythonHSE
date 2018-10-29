N = int(input())
res = 0
res2 = 0
N1 = 1
i = 0
M = 1
while M <= N:
    N1 = M
    res2 = 0
    res = 0
    while N1 != 0:
        res2 = res2 * 10
        res = N1 % 10
        res2 = res2 + res
        N1 = (N1 - res) // 10
    if res2 == M:
        i += 1
    M += 1
print(i)
