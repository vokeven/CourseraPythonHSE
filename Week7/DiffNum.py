# Дан список чисел, который может содержать до 100000 чисел.
# Определите, сколько в нем встречается различных чисел.


if __name__ == '__main__':
    n = set(map(int,input().split()))
    num = len(n)
    print(num)
