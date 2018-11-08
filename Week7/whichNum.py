# Август и Беатриса играют в игру. Август загадал натуральное
# число от 1 до n. Беатриса пытается угадать это число, для
# этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES, если среди названных ей чисел
# есть задуманное или NO в противном случае. После нескольких
# заданных вопросов Беатриса запуталась в том, какие вопросы
# она задавала и какие ответы получила и просит вас помочь ей
# определить, какие числа мог задумать Август.

if __name__ == '__main__':
    n = int(input())
    noSet = set()
    yesSet = set()
    m = input().strip().split()
    while m[0] != 'HELP':
        m = list(map(int, m))
        ans = input().strip()
        s = set(m)
        if ans == 'NO':
            noSet.update(s)
        else:
            if yesSet == set():
                yesSet = s
            else:
                yesSet &= s
        m = input().strip().split()
    if yesSet == set():
        yesSet = set(i for i in range(1, n+1))
    res = yesSet - noSet
    resList = list(res)
    resList.sort()
    print(*resList)
