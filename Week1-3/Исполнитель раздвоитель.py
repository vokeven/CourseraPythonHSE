A = int(input())
B = int(input())
X = A
while X != B:
    if X % 2 == 0 and X // 2 >= B:
        X = X // 2
        print(':2')
    else:
        X = X - 1
        print('-1')
