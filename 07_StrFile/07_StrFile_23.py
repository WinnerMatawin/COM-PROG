c = input().split()
name = c[0]
x = (c[1])[2:]
fn = open(name, 'r')
l = []
s = []
for line in fn :
    a,b = line.split()
    l.append([float(b), a])
l.sort()
for t in l :
    if (t[1])[:2] == x :
        s.append(t[0])
if len(s) == 0 :
    print('No data')
else:
    print(min(s), max(s), sum(s)/len(s))


fn.close()
