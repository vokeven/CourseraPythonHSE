# Дан список целых чисел. Требуется “сжать” его,
# переместив все ненулевые элементы в левую часть списка,
# не меняя их порядок, а все нули - в правую часть.
# Порядок ненулевых элементов изменять нельзя,
# дополнительный список использовать нельзя,
# задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.


def gripList(xList):
    i = 0
    k = 0
    while i < len(xList):
        if xList[i] == 0:
            j = i + 1
            while j < len(xList) and xList[j] == 0:
                j += 1
            else:
                if j == len(xList):
                    pass
                elif xList[j] != 0:
                    xList[k], xList[j] = xList[j], xList[i]
                    k += 1
            i = j + 1
        else:
            xList[k], xList[i] = xList[i], xList[k]
            i += 1
            k += 1
    return xList


xList = list((map(int, input().split())))
print(*gripList(xList))
# print(*gripList([0,1,0,1,0]))
# print(*gripList([0,0,1,1,0]))
# print(*gripList([5,1,0,1,0]))
# print(*gripList([0,1,0,1,5]))
