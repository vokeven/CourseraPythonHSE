# Выведите значение наименьшего из всех положительных элементов в списке.
# Известно, что в списке есть хотя бы один положительный элемент,
# а значения всех элементов списка по модулю не превосходят 1000.


def isMin(xList):
    minX = 999
    for i in range(len(xList)):
        if xList[i] > 0 and minX > xList[i]:
            minX = xList[i]
    return minX


xList2 = list(map(int, input().split()))
print(isMin(xList2))
