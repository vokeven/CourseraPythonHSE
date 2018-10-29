N = int(input())
if 10 < N < 20 or N % 10 in (0, 5, 6, 7, 8, 9):
    print(N, 'korov')
elif N % 10 == 1:
    print(N, "korova")
else:
    print(N, 'korovy')
