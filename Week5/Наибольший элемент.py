# Дан список чисел. Выведите значение наибольшего элемента в списке,
# а затем индекс этого элемента в списке.
# Если наибольших элементов несколько, выведите индекс первого из них.


def isMax(xList):
    maxX = xList[0]
    maxI = 0
    for i in range(len(xList)-1, -1, -1):
        if maxX <= xList[i]:
            maxX = xList[i]
            maxI = i
    return maxX, maxI


xList2 = list(map(int, input().split()))
print(*isMax(xList2))
