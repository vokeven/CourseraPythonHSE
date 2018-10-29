# В данном списке из n≤10⁵ целых чисел найдите три числа,
# произведение которых максимально.
# Решение должно иметь сложность O(n), где n - размер списка.
# Выведите три искомых числа в любом порядке.


def maxN(xList):
    (min1, min2, min3, max1, max2, max3) = (
        None, None, None, None, None, None)
    for i in xList:
        if min1 is None:
            min1 = i
        elif min2 is None:
            if i <= min1:
                min2, min1 = min1, i
            else:
                min2 = i
        elif min3 is None:
            if i <= min1:
                min1, min2, min3 = i, min1, min2
            elif i <= min2:
                min2, min3 = i, min2
            else:
                min3 = i
            max1, max2, max3 = min1, min2, min3
        elif i > max1:
            if i >= max2:
                if i >= max3:
                    max3, max2, max1 = i, max3, max2
                else:
                    max2, max1 = i, max2
            else:
                max1 = i
        elif i < min3:
            if i <= min2:
                if i <= min1:
                    min1, min2, min3 = i, min1, min2
                else:
                    min2, min3 = i, min2
            else:
                min3 = i
    l2 = [min1, min2, min3, max1, max2, max3]
    # print(l2)

    for j in range(len(l2)):
        if l2[j] == 0:
            l2[j] = 1

    if min2 < 0:
        if max3 > 0:
            a = min1 * min2 * max3
            b = max1 * max2 * max3
            if a > b:
                print(min1, min2, max3)
            else:
                print(max1, max2, max3)
        else:
            print(max1, max2, max3)
    else:
        print(max1, max2, max3)

xList = list((map(int, input().split())))
maxN(xList)
