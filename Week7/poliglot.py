# Каждый из N школьников некоторой школы знает Mᵢ языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.

if __name__ == '__main__':
    n = int(input())
    allLang = set()
    allScolar = set()
    for k in range(n):
        m = int(input())
        langM = set()
        if k == 0:
            allScolar = langM
        for i in range(m):
            lang = input().strip().split()
            allLang.update(lang)
            langM.update(lang)
        allScolar &= langM
    print(len(allScolar))
    for y in allScolar:
        print(y)
    print(len(allLang))
    for x in allLang:
        print(x)
