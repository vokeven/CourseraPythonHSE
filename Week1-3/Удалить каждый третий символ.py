t = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 1], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1],
     [0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 1, 0],
     [0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 1],
     [0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 1], [0, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 0, 1],
     [0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 1, 1],
     [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 0, 1, 1, 0, 0],
     [1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1],
     [1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1], [1, 1, 0, 1, 0, 0], [1, 1, 0, 1, 0, 1], [1, 1, 0, 1, 1, 0],
     [1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0], [1, 1, 1, 0, 1, 1],
     [1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1]]
res = 0
for i in t:
    a = i[0]
    b = i[1]
    c = i[2]
    d = i[3]
    e = i[4]
    f = i[5]

    delta = a * d - b * c
    if delta != 0:
        deltaX = e * d - f * b
        deltaY = a * f - c * e
        x = deltaX / delta
        y = deltaY / delta
        print(2, x, y)
    else:
        if (a, b, c, d, e, f) == (0, 0, 0, 0, 0, 0):
            print(5)
        elif (a, b, c, d) == (0, 0, 0, 0):
            print(0)
        elif (a, c) == (0, 0) and b * f == e * d:
            if b != 0:
                y = e / b
                print(4, y)
            else:
                y = f / d
                print(4, y)
        elif (a, c) == (0, 0):
            print(0)
        elif (b, d) == (0, 0) and a * f == c * e:
            if a != 0:
                x = e / a
                print(3, x)
            else:
                x = f / c
                print(3, x)
        elif (b, d) == (0, 0):
            print(0)
        elif (a + b) * f == (c + d) * e and b != 0:
            p = -a / b
            q = e / b
            print(1, p, q)

    print(a, b, e)
    print(c, d, f)
    print(res)
    print('--------')

