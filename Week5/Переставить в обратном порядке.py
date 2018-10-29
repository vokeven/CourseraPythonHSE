# Переставьте элементы данного списка в обратном порядке,
# затем выведите элементы полученного списка.
# Эта задача отличается от предыдущей тем, что вам
# нужно изменить значенияэлементов самого списка,
# поменяв местами A[0] c A[n-1],A[1] с A[n-2],
# а затем вывести элементы списка подряд.


def reverseList(xList):
    yList = []
    for i in range(len(xList)-1, -1, -1):
        yList.append(xList[i])
    xList = yList
    return xList


newList = list(map(int, input().split()))
print(*reverseList(newList))
