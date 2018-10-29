A = int(input())
B = int(input())
K = int(input())
if ((K % A == 0) or (K % B == 0)) and K <= A * B:
    print('YES')
else:
    print("NO")
