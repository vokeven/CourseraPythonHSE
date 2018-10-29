def sumN():
    n = int(input())
    if n != 0:
        return sumN() + n
    else:
        return 0


print(sumN())
