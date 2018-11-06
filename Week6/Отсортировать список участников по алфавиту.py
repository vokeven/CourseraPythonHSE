# -*- coding: utf-8 -*-

# Известно, что фамилии всех участников — различны.
# Сохраните в массивах список всех участников и выведите его,
# отсортировав по фамилии в лексикографическом порядке.
# При выводе указываете фамилию, имя участника и его балл.
#
# Используйте для ввода и вывода файлы input.txt и output.txt
# с указанием кодировки utf8. Например, для чтения откройте
# файл с помощью open('input.txt', 'r', encoding='utf8').


def olympiada():
    with open('input.txt', 'r', encoding='utf-8') as f_in:
        new = []
        for line in f_in:
            s = line.strip().split()
            new.append(s)
    new.sort()
    new3 = []
    for x in new:
        y = [0] * 3
        y[0] = x[0]
        y[1] = x[1]
        y[2] = x[3]
        new3.append(y)
    with open('output.txt', 'w', encoding='utf-8') as f_out:
        for line2 in new3:
            print(*line2, file=f_out)
    return


olympiada()
