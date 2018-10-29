N = int(input())
X = 1
if N == X:
    print('YES')
else:
    X = 2
    while X < N:
        X += X
    if N == X:
        print('YES')
    else:
        print('NO')
