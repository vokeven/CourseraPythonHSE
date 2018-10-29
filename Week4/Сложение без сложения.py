def sum(a, b):
    if a > 0:
        return sum(a - 1, b) + 1
    elif b > 0:
        return sum(a, b - 1) + 1
    else:
        return 0


a = int(input())
b = int(input())
print(sum(a, b))
