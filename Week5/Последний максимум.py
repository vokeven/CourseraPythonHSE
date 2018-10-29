# Дан список чисел. Выведите все элементы списка,
# которые больше предыдущего элемента.

xList = list(map(int, input().split()))
maxX = xList[0]
maxI = 0

for i in range(len(xList)):
    if maxX <= xList[i]:
        maxX = xList[i]
        maxI = i
print(maxX, maxI)
