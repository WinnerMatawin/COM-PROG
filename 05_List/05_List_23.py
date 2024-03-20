x = []
n = int(input())
for i in range(1,n+1):
    a,b = input().split()
    dis = (float(a)**2 + float(b)**2)**0.5
    x.append([dis, i, a, b])
x.sort()
print('#' + str((x[2])[1]) + ':', '('+str((x[2])[2])+', '+str((x[2])[3])+')')
    
