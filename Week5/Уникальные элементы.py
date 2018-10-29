# Дан список. Выведите те его элементы,
# которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке,
# в котором они встречаются в списке.


from collections import defaultdict

def unique(xList):
    for i in xList:

inList = list(map(int, input().split()))
print(isMin(inList))
