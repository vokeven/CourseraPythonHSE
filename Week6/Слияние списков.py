# Даны два целочисленных списка A и B, упорядоченных по неубыванию.
# Объедините их в один упорядоченный список С (то есть он должен
# содержать len(A)+len(B) элементов). Решение оформите в виде функции
# merge(A, B), возвращающей новый список. Алгоритм должен иметь
# сложность O(len(A)+len(B)). Модифицировать исходные списки
# запрещается. Использовать функцию sorted и метод sort запрещается.


def merge(a, b):
    i, j = 0, 0
    c = []
    while i <= len(a) and j <= len(b):
        if i == len(a):
            if j == len(b):
                return c
            else:
                c.append(b[j])
                j += 1
        elif j == len(b):
            c.append(a[i])
            i += 1
        elif a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c


a = list((map(int, input().split())))
b = list((map(int, input().split())))
print(*merge(a, b))
