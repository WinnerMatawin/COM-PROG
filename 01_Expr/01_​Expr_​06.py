h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

# h2 >=h1 or h2 < h1
t1 = m1*60 + s1
t2 = m2*60 + s2
dh_new = ((24 + (h2 - h1)) % 24)
dt = dh_new*60*60 + t2 - t1
dh_new = dt // (60*60) 
dt -= dh_new * 60*60
dm = dt // 60
dt -= dm*60
ds = dt
if dh_new < 0:
    dh_new += 24
print(str(dh_new)+":"+str(dm)+":"+str(ds))
