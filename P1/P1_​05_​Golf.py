#not checked
a = []
b = []
c = []
for i in range(9) :
    p = [int(e) for e in input().split()]
    a += [p[0]]
    b += [p[1]]
    c += [p[2]]
d = []
for i in range(9) :
    d.append(min(b[i],a[i]+2))
sum_a = sum(a)
sum_b = sum(b)
d_set = []
for i in range(9) :
    if c[i] ==1 :
        d_set.append(d[i])
sum_d = sum(d_set)
t = int((0.8*(1.5*sum_d-sum_a))//1)
net = sum_b - t
print(sum_b)
print(t)
print(net)
