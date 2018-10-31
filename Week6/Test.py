def mySum(*args):
    print(args)
    nowSum = 0
    for now in args:
        nowSum += now
    return nowSum

print(mySum(1, 2))
print(mySum(1, 2, 3, 4))
