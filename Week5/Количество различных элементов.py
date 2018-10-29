# Дан список, упорядоченный по неубыванию элементов в нем.
# Определите, сколько в нем различных элементов.


def differenceElem(xList):
    numX = 1
    for i in range(len(xList)-1):
        if xList[i] != xList[i+1]:
            numX += 1
    return numX


xList = list((map(int, input().split())))
print(differenceElem(xList))
