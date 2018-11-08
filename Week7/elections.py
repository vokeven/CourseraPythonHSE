# -*- coding: utf-8 -*-
# В выборах Президента Российской Федерации побеждает кандидат,
# набравший свыше половины числа голосов избирателей.
# Если такого кандидата нет, то во второй тур выборов
# выходят два кандидата, набравших наибольшее число голосов.

import sys
from collections import defaultdict


def main():
    winner()


def winner():
    dict = defaultdict(int)
    count = 0
    with open('input.txt', encoding='utf-8') as f:
        for line in f:
            man = line.strip()
            dict[man] += 1
            count += 1
    list_man = list(dict.items())
    list_man.sort(key=lambda x: x[1], reverse=True)
    with open('output.txt', 'w', encoding='utf-8') as f_out:
        if list_man[0][1] > count // 2:
            f_out.write(list_man[0][0])
        else:
            f_out.write(list_man[0][0] + '\n')
            f_out.write(list_man[1][0])


if __name__ == '__main__':
    main()
