import math
n = int(input())
mylist = [str(n)]
while n != 1 :
    if n%2 == 0 :
        n = round((n/2)//1)
    else:
        n = 3*n + 1
    mylist.append(str(n))
if len(mylist) > 15 :
    mylist = mylist[-15:]
print("->".join(mylist))
