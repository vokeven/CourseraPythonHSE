# -*- coding: utf-8 -*-
# Вам дан словарь, состоящий из пар слов.
# Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны. Для одного данного
# слова определите его синоним.

from collections import defaultdict


def main():
    seek_synonym()


def seek_synonym():
    n = int(input())
    dict_syn = defaultdict(str)
    for i in range(n):
        line = input()
        key, value = tuple(line.split())
        dict_syn[key] = value
        dict_syn[value] = key
    seek = input()
    print(dict_syn[seek])


if __name__ == '__main__':
    main()
