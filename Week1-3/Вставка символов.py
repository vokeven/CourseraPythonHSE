n = int(input())
def MinDivisor(n):
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            print(i)
            break
        elif i == n ** 0.5:
            print(n)
        i += 1
