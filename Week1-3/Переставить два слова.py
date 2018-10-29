s = input()
space = s.find(' ')
s = s[space + 1:] + ' ' + s[:space]
print(s)
