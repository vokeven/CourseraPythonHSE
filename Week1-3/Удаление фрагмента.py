s = input()
hLeft = s.find('h')
hRight = s.rfind('h')
s = s[:hLeft] + s[hRight+1:]
print(s)
