s = input()
hLeft = s.find('h')
hRight = s.rfind('h')
s = s[:hLeft+1] + (s[hLeft+1:hRight] * 2) + s[hRight:]
print(s)
