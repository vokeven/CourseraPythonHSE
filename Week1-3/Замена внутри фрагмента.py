s = input()
s = s.replace('h', 'H')
s = s[:s.find('H')] + 'h' + s[s.find('H') + 1:]
s = s[:s.rfind('H')] + 'h' + s[s.rfind('H') + 1:]
print(s)
