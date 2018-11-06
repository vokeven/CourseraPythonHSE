# Дан список из N (N≤2*10⁵) элементов, которые принимают
# целые значения от 0 до 100.
# Отсортируйте этот список в порядке неубывания элементов.
# Выведите полученный список.
# Решение оформите в виде функции CountSort(A), которая модифицирует
# передаваемый ей список. Использовать встроенные функции сортировки нельзя.


def countSort(a):
    xList = [0] * 101
    for j in a:
        xList[j] += 1
    res = []
    for ind, k in enumerate(xList):
        if k != 0:
            for z in range(k):
                res.append(ind)
    return res


if __name__ == '__main__':
    n = list(map(int, input().split()))
    print(*countSort(n))
