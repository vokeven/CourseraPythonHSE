# -*- coding: utf-8 -*-
# В олимпиаде по информатике принимало участие несколько человек.
#
# Определите и выведите средние баллы участников олимпиады в
# 9 классе, в 10 классе, в 11 классе.


def olympiada():
    with open('c:\\input2.txt', 'r', encoding='utf-8') as f:
        res = [0] * 6
        for line in f:
            s = line.strip().split()
            if int(s[2]) == 9:
                res[0] += int(s[3])
                res[1] += 1
            elif int(s[2]) == 10:
                res[2] += int(s[3])
                res[3] += 1
            elif int(s[2]) == 11:
                res[4] += int(s[3])
                res[5] += 1
    if res[1] == 0:
        res[1] = 1
    if res[3] == 0:
        res[3] = 1
    if res[5] == 0:
        res[5] = 1
    res_final = [res[0]/res[1], res[2]/res[3], res[4]/res[5]]
    print(* res_final)
    return res_final


olympiada()
