def reverseSqr():
    n = int(input())
    i = 0
    if n != 0:
        i = i + reverseSqr()
        if int(n ** 0.5) ** 2 == n:
            print(n, end=' ')
            return 1
        else:
            return i
    else:
        return i

if reverseSqr() < 1:
    print(0)
