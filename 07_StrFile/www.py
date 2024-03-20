a = input().lower()
b = input().lower()
s1 = []
for e in a :
    if '0' <= e <= '9' or 'a' <= e < 'z' :
        s1.append(e)
s2 = []
for e in b :
    if '0' <= e <= '9' or 'a' <= e < 'z' :
        s2.append(e)
s1.sort()
s2.sort()
if s1 == s2 :
    print('YES')
else:
    print('NO')