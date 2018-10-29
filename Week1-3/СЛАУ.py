a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
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
    elif (a, b) == (0, 0) and e != 0:
        print(0)
    elif (c, d) == (0, 0) and f != 0:
        print(0)
    elif (a, c) == (0, 0) and b * f == e * d:
        if b != 0 and d != 0:
            y = e / b
            print(4, y)
        else:
            print(0)
    elif (b, d) == (0, 0) and a * f == c * e:
        if a != 0 and c != 0:
            x = e / a
            print(3, x)
        else:
            print(0)
    elif (a + b) * f == (c + d) * e and b != 0:
        p = -a / b
        q = e / b
        print(1, p, q)
    else:
        print(0)
