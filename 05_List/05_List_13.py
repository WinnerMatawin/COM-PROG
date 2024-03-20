mylist = []
n = int(input())
for i in range(n) :
    mylist.append(int(input()))
sec = [int(e) for e in input().split()]
mylist += sec
e = int(input())
while True :
    if e == -1:
        break
    mylist.append(e)
    e = int(input())
ans = []
for i in range(len(mylist)) :
    if i%2 == 0:
        ans.append(mylist[i])
    else: ans.insert(0,mylist[i])
print(ans)
        
