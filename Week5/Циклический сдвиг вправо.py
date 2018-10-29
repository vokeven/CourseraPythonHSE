# Циклически сдвиньте элементы списка вправо(A[0]
# переходит на место A[1], A[1] на место A[2], ...,
# последний элемент переходит на место A[0]).


def rightShift(xList):
    a = xList[-1]
    for i in range(len(xList)-1, 0, -1):
        xList[i] = xList[i-1]
    xList[0] = a
    return xList

newList = list((map(int, input().split())))
print(*rightShift(newList))
