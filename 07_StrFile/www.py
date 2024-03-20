x = input()
s = ''
for i in range(len(x)) :
    if x[i] not in ' \- \" \- \( \) \. \] \[ \! \< \> \, \; \;' :
        s += x[i]
    else : s += ' '
t = s.split()
print(t[0].lower(), end = '')
for i in range(1,len(t)) :
    print((t[i])[0].upper() + (t[i])[1:].lower(), end = '')