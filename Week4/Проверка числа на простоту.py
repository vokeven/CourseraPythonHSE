def IsPrime(n):
    """ Check if number (n) is prime """
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            return False
        i += 1
    if i > n ** 0.5:
        return True


n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
