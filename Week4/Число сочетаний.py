def C(n, k):
    if k == n:
        return 1
    elif k == 1:
        return n
    elif k == 0:
        return 1
    return C(n - 1, k) + C(n - 1, k - 1)


n = int(input())
k = int(input())

print(C(n, k))
