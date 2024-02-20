d = int(input())
m = int(input())
y = int(input())
y -= 543
mlist = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if y%400 == 0 or y%4==0 and y%100 !=0 :
    mlist[2] = 29

dayofyear = d + sum(mlist[:m])
print(dayofyear)
