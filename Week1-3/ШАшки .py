X1 = int(input())
Y1 = int(input())
X2 = int(input())
Y2 = int(input())
XX = (X2 - X1) % 2
YY = (Y2 - Y1) % 2
if ((XX == 0 and YY == 0) or (XX != 0 and YY != 0)) and (Y2 - Y1 > 0):
    print('YES')
else:
    print('NO')
