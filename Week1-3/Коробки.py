A1 = int(input())
B1 = int(input())
C1 = int(input())
A2 = int(input())
B2 = int(input())
C2 = int(input())
if C1 <= A1 <= B1:
    A1, B1, C1 = C1, A1, B1
elif A1 <= C1 <= B1:
    A1, B1, C1 = A1, C1, B1
elif C1 <= B1 <= A1:
    A1, B1, C1 = C1, B1, A1
elif B1 <= C1 <= A1:
    A1, B1, C1 = B1, C1, A1
elif B1 <= A1 <= C1:
    A1, B1, C1 = B1, A1, C1
else:
    A1, B1, C1 = A1, B1, C1
if C2 <= A2 <= B2:
    A2, B2, C2 = C2, A2, B2
elif A2 <= C2 <= B2:
    A2, B2, C2 = A2, C2, B2
elif C2 <= B2 <= A2:
    A2, B2, C2 = C2, B2, A2
elif B2 <= C2 <= A2:
    A2, B2, C2 = B2, C2, A2
elif B2 <= A2 <= C2:
    A2, B2, C2 = B2, A2, C2
else:
    A2, B2, C2 = A2, B2, C2
if A1 == A2 and B1 == B2 and C1 == C2:
    print('Boxes are equal')
elif A1 <= A2 and B1 <= B2 and C1 <= C2:
    print('The first box is smaller than the second one')
elif A1 >= A2 and B1 >= B2 and C1 >= C2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
