# Даны два списка чисел, которые могут содержать до 10000
# чисел каждый. Выведите все числа, которые входят как в
# первый, так и во второй список, в порядке возрастания.

if __name__ == '__main__':
    n1 = set(map(int, input().split()))
    n2 = set(map(int, input().split()))
    num = list(n1 & n2)
    num.sort()
    print(*num)
