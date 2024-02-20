a = list(map(float, input().split()))

#find max
next = a[1]
max = a[0]
index_max = 0
for i in range(3) :
    next = a[i+1]
    if max < next :
        max = next
        index_max  = i + 1
    if i == 3 :
        break
    

#find min
next = a[1]
index_min = 0
min = a[0]
for i in range(3) :
    next = a[i+1]
    if min > next :
        min = next
        index_min = i + 1
    if i == 3 :
        break
    
    
a[index_max] = 0
a[index_min] = 0
mean = sum(a)/2
print(round(mean,2))