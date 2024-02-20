n = int(input())
x = []
y = []
p = []
q = []
for i in range(n):
    a = list(map(int,input().split()))
    x.append(a[0])
    y.append(a[1])
    a = []
z = input()
if z == '''Zig-Zag''':
    for i in range(0,n,2) :
        p.append(x[i])
        q.append(y[i])
    for i in range(1,n,2) :
        p.append(y[i])
        q.append(x[i])
else :
    for i in range(0,n,2) :
        p.append(y[i])
        q.append(x[i])
    for i in range(1,n,2) :
        p.append(x[i])
        q.append(y[i])
print(min(p), max(q))
