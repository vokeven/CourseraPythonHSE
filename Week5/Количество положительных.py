# Найдите количество положительных элементов в данном списке.

xList = list(map(int, input().split()))
numX = 0

for i in range(len(xList)):
    if xList[i] > 0:
        numX += 1
print(numX)
