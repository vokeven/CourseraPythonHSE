def reverse():
    n = int(input())
    if n != 0:
        reverse()
        return print(n)
    else:
        return print(n)

reverse()
