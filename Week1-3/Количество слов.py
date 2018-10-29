s = input()
k = 1
while s.find(' ') != -1:
    k += 1
    pos = s.find(' ')
    s = s[pos + 1:]
print(k)
