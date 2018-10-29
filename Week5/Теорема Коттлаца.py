for j in range(2, 10000000):
    x = 0
    while j != 1:
        if j % 2 == 0:
            j = j / 2
        else:
            j = 3 * j + 1
        x += 1
    if x > 500:
        print(x)
