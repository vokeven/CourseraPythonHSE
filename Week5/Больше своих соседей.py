# Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше двух своих соседей и выведите количество таких элементов.


def isBigger(xList):
    numX = 0
    for i in range(1, len(xList)-1):
        if xList[i-1] < xList[i] > xList[i+1]:
            numX += 1
    return numX

xList2 = list(map(int, input().split()))
print(isBigger(xList2))
