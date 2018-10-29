# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.

from collections import defaultdict


def doubles(xList):
    sumN = 0
    for i in range(len(xList)-1):
        for j in range(i+1, len(xList)):
            if xList[i] == xList[j]:
                sumN += 1
    return sumN


xList = list((map(int, input().split())))
print(doubles(xList))
