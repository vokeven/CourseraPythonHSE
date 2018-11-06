# В олимпиаде участвовало N человек. Каждый получил определенное
# количество баллов, при этом оказалось, что у всех участников
# разное число баллов. Упорядочите список участников олимпиады
# в порядке убывания набранных баллов.


def sortMan(xList):
    newList = []
    for member in xList:
        FIO = member.split()[0]
        score = int(member.split()[1])
        newList.append([score, FIO])
    newList.sort(reverse=True)
    for line in newList:
        print(line[1])
    return newList


if __name__ == '__main__':
    n = int(input())
    olympList = [input() for i in range(n)]
    sortMan(olympList)
