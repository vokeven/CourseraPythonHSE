# Дан список. Не изменяя его и не используя дополнительные списки,
# определите, какое число в этом списке встречается чаще всего.
# Если таких чисел несколько, выведите любое из них.

from collections import defaultdict


def maxN(xList):
    dic = defaultdict(int)
    maxD = 0
    maxJ = xList[0]
    for num in xList:
        dic[num] += 1
    for j in dic:
        if maxD <= dic[j]:
            maxD = dic[j]
            maxJ = j
    return maxJ

xList = list((map(int, input().split())))
print(maxN(xList))
