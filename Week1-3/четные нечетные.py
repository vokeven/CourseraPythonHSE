A = int(input())
B = int(input())
C = int(input())
A2 = A % 2
B2 = B % 2
C2 = C % 2
if (A2 == 0 or B2 == 0 or C2 == 0) and (A2 != 0 or B2 != 0 or C2 != 0):
    print('YES')
else:
    print('NO')
