# Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
# Если элементов нечетное число, то последний элемент остается на своем месте


def changeElem(xList):
    i = 0
    while i < len(xList) - 1:
        xList[i], xList[i+1] = xList[i+1], xList[i]
        i += 2
    return xList


xList = list((map(int, input().split())))
print(*changeElem(xList))
