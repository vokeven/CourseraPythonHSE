A = int(input())
B = int(input())
C = int(input())
if A > B:
    if A > C:
        print(A)
    else:
        print(C)
else:
    if B > C:
        print(B)
    else:
        print(C)
