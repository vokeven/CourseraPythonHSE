A = int(input())
B = int(input())
C = int(input())
if C <= A <= B:
    A, B, C = C, A, B
elif A <= C <= B:
    A, B, C = A, C, B
elif C <= B <= A:
    A, B, C = C, B, A
elif B <= C <= A:
    A, B, C = B, C, A
elif B <= A <= C:
    A, B, C = B, A, C
else:
    A, B, C = A, B, C
print(A, B, C)
