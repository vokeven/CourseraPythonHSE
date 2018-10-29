def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    return a

a = int(input())
b = int(input())
print(gcd(a, b))
