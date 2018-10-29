A1 = int(input())
B1 = int(input())
C1 = int(input())
A2 = int(input())
B2 = int(input())
C2 = int(input())
N = 0
N1 = (C1 // C2) * (A1 // A2) * (B1 // B2)
N2 = (C1 // A2) * (A1 // B2) * (B1 // C2)
N3 = (C1 // B2) * (A1 // C2) * (B1 // A2)
N4 = (C1 // C2) * (A1 // B2) * (B1 // A2)
N5 = (C1 // A2) * (A1 // C2) * (B1 // B2)
N6 = (C1 // B2) * (A1 // A2) * (B1 // C2)
if N1 >= N2 and N1 >= N3 and N1 >= N4 and N1 >= N5 and N1 >= N6:
    N = N1
elif N2 >= N1 and N2 >= N3 and N2 >= N4 and N2 >= N5 and N2 >= N6:
    N = N2
elif N3 >= N1 and N3 >= N2 and N3 >= N4 and N3 >= N5 and N3 >= N6:
    N = N3
elif N4 >= N1 and N4 >= N2 and N4 >= N3 and N4 >= N5 and N4 >= N6:
    N = N4
elif N5 >= N2 and N5 >= N3 and N5 >= N4 and N5 >= N1 and N5 >= N6:
    N = N5
elif N6 >= N2 and N6 >= N3 and N6 >= N4 and N6 >= N5 and N6 >= N1:
    N = N6
print(N)
