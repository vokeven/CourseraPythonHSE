i = 0
N = int(input())
while N != 0:
    N2 = int(input())
    if N2 > N:
        i += 1
    N = N2
print(i)
