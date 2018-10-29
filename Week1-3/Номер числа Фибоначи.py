A = int(input())
k = 1
fibNum1 = 0
fibNum2 = 1
fibNumN = 0
if A == 0:
    k = 0
    print(k)
elif A == 1:
    k = 1
    print(k)
else:
    while A > fibNum2:
        k += 1
        fibNumN = fibNum2 + fibNum1
        fibNum1, fibNum2 = fibNum2, fibNumN
    if A != fibNumN:
        print(-1)
    else:
        print(k)
