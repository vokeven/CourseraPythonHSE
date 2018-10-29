# Дан список, заполненный произвольными целыми числами.
# Найдите в этом списке два числа, произведение которых максимально.
# Выведите эти числа в порядке неубывания.
#
# Решение должно иметь сложность O(n), где n - размер списка.


def max2(xList):
    (minL, minH, maxL, maxH) = (xList[0], xList[0], xList[0], xList[0])
    for i in xList:
        if i <= minH:
            if i <= minL:
                minH = minL
                minL = i
            else:
                minH = i
        if i >= maxL:
            if i >= maxH:
                maxL = maxH
                maxH = i
            else:
                maxL = i
    if maxL * maxH > minL * minH:
        return maxL, maxH
    else:
        return minL, minH


xList = list((map(int, input().split())))
print(*max2(xList))
