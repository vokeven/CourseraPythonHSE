A = int(input())
B = int(input())
C = int(input())
D = int(input())
X2 = (A - C)**2 % 2
Y2 = (B - D)**2 % 2
if (X2 == 0 and Y2 == 0) or (X2 != 0 and Y2 != 0):
    print('YES')
else:
    print("NO")
