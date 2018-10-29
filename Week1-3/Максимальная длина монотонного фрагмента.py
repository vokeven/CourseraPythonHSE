n = int(input())
maxN = 1
up = 1
down = 1
if n == 0:
    maxN = 0
while n != 0:
    n2 = int(input())
    if n2 > n and down == 1:
        up += 1
        if maxN < up:
            maxN = up
    elif n2 > n and down > 1:
        up = 2
        down = 1
    elif n2 < n and up > 1 and n2 != 0:
        down = 2
        up = 1
    elif n2 < n and up == 1 and n2 != 0:
        down += 1
        if maxN < down:
            maxN = down
    elif n2 == n:
        up = 1
        down = 1
    n = n2
print(maxN)
