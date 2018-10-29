# Дан список чисел. Выведите все элементы списка,
# которые больше предыдущего элемента.

xList = list(map(int, input().split()))

for i in range(1, len(xList)):
    if xList[i] > xList[i-1]:
        print(xList[i], end=' ')
