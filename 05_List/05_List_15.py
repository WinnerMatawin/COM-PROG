x = [int(e) for e in input().split()]
x.sort()
c = 1
ans = []
a = x[0]
for i in range(len(x)) :
    if x[i] != a :
        c += 1
        ans.append(a)
        a = x[i]
ans.append(a)
print(c)
print(ans[:10])
