# -*- coding: utf-8 -*-
# Дан текст. Выведите все слова, встречающиеся в тексте,
# по одному на каждую строку. Слова должны быть отсортированы
# по убыванию их количества появления в тексте, а при
# одинаковой частоте появления — в лексикографическом порядке.

import sys
from collections import defaultdict


def main():
    sort_by_frequency()


def sort_by_frequency():
    f = sys.stdin.read()
    wordList = f.split()
    dict_word = defaultdict(int)
    for word in wordList:
        dict_word[word] -= 1
    list_word = list(dict_word.items())
    list_word.sort(key=lambda word: (word[1], word[0]))
    for x in list_word:
        print(x[0])


if __name__ == '__main__':
    main()
