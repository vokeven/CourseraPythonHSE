# Выведите элементы данного списка в обратном порядке,
# не изменяя сам список.


def reverseList(xList):
    for i in range(len(xList) - 1, -1, -1):
        print(xList[i], end=' ')


mList = list(map(int, input().split()))
reverseList(mList)
