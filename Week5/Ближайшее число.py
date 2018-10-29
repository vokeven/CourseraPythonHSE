# Напишите программу, которая находит в массиве элемент,
# самый близкий по величине к данному числу.


def nearElem(xList, x):
    difX = 2000
    minN = xList[0]
    for i in xList:
        if (x - i) ** 2 < difX ** 2:
            difX = x - i
            minN = i
    return minN


n = int(input())
newList = list((map(int, input().split())))
x = int(input())
print(nearElem(newList, x))
