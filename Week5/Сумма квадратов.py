# По данному натуральном n вычислите сумму 1²+2²+3²+...+n².

n = int(input())
sumN = 0

for i in range(1, n + 1):
    sumN += i * i

print(sumN)
