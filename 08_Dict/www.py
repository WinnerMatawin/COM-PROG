t = input().lower()
count = {}
for e in t :
    if 'a'<=e<='z':
        if e in count :
            count[e] += 1
        else:
            count[e] = 1
x = []
for k in count :
    x.append([-count[k],k])
x.sort()
for cnt, k in x :
    print(k, '->', -cnt)