# В олимпиаде по информатике принимало участие несколько человек.
# Победителем олимпиады становится человек, набравший больше всех
# баллов. Победители определяются независимо по каждому классу.
# Определите количество баллов, которое набрал победитель в каждом
# классе. Гарантируется, что в каждом классе был хотя бы один участник.


def calcMaxScore(path_):
    with open(path_, 'r', encoding='utf-8') as f_in:
        max9, max10, max11 = 0, 0, 0
        for line in f_in:
            s = line.strip().split()
            if int(s[2]) == 9:
                if int(s[3]) > max9:
                    max9 = int(s[3])
            elif int(s[2]) == 10:
                if int(s[3]) > max10:
                    max10 = int(s[3])
            else:
                if int(s[3]) > max11:
                    max11 = int(s[3])
    return list((max9, max10, max11))


if __name__ == '__main__':
    path_ = 'input.txt'
    print(*calcMaxScore(path_))
