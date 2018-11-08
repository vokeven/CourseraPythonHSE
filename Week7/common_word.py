# -*- coding: utf-8 -*-
# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше
# в лексикографическом порядке.

import sys
from collections import defaultdict


def main():
    count_word()


def count_word():
    f = sys.stdin.read()
    list_word = f.split()
    dict_word = defaultdict(int)
    for word in list_word:
        dict_word[word] -= 1
    list_dict = list(dict_word.items())
    list_dict.sort(key=lambda x: (x[1], x[0]))
    print(list_dict[0][0])


if __name__ == '__main__':
    main()
