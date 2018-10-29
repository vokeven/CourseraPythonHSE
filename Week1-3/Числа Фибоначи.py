N = int(input())
k = 1
fibNum1 = 0
fibNum2 = 1
fibNumN = 0
if N == 1:
    fibNumN = 1
while k < N:
    fibNumN = fibNum2 + fibNum1
    fibNum1, fibNum2 = fibNum2, fibNumN
    k += 1
print(fibNumN)
