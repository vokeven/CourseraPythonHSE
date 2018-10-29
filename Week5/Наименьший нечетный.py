# Выведите значение наименьшего нечетного элемента списка,
# гарантируется, что хотя бы один нечётный элемент в списке есть.


def isMin(xList):
    i = 0
    while xList[i] % 2 == 0:
        i += 1
    minX = xList[i]

    for j in range(i, len(xList)):
        if xList[j] % 2 != 0 and minX > xList[j]:
            minX = xList[j]
    return minX


xList2 = list(map(int, input().split()))
print(isMin(xList2))
