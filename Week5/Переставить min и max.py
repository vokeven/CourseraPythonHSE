# В списке все элементы попарно различны.
# Поменяйте местами минимальный и максимальный элемент этого списка.


def exchangeMinMax(xList):
    minX, maxX = xList[0], xList[0]
    minI, maxI = 0, 0
    for i, num in enumerate(xList):
        if num < minX:
            minX = num
            minI = i
        if num > maxX:
            maxX = num
            maxI = i
    xList[minI] = maxX
    xList[maxI] = minX
    return xList


xList = list((map(int, input().split())))
print(*exchangeMinMax(xList))
