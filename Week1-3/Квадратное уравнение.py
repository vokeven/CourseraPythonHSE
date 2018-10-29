a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
x, x1, x2 = None, None, None
if a != 0:
    if d < 0:
        print(0)
    elif d == 0:
        x1 = -b / (2 * a)
        print(1, x1)
    elif d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        if x1 > x2:
            x1, x2 = x2, x1
        print(2, x1, x2)
elif b != 0:
    x = -c / b
    print(1, x)
elif c != 0:
    print(0)
else:
    print(3)
