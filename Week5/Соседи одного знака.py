# Дан список чисел. Если в нем есть два соседних элемента одного знака,
# выведите эти числа. Если соседних элементов одного знака нет -
# не выводите ничего. Если таких пар соседей несколько - выведите первую пару


def isLike(xList):
    for i in range(len(xList)-1):
        if xList[i] * xList[i+1] > 0:
            return xList[i:i+2]
    return 0

xList2 = list(map(int, input().split()))
if isLike(xList2) == 0:
    pass
else:
    print(*isLike(xList2))
