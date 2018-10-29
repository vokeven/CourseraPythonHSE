s = input()
if s.find('f') != -1:
    pos = s.find('f')
    s = s[pos+1:]
    if s.find('f') != -1:
        print(s.find('f') + pos + 1)
    else:
        print(-1)
else:
    print(-2)
