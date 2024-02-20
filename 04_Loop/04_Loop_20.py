x,y = input().split()
x,y = int(x), int(y)
i = 2
min_zigzag = x
max_zigzag = y
min_zagzig = y
max_zagzig = x
while True :
    d = input().split()
    if len(d) == 1 : break
    x, y = int(d[0]), int(d[1])
    if i%2 ==1 :
        min_zigzag = min(x,min_zigzag) 
        max_zigzag = max(y,max_zigzag)
        min_zagzig = min(y,min_zagzig)
        max_zagzig = max(x,max_zagzig)
    else:
        min_zigzag = min(y,min_zigzag) 
        max_zigzag = max(x,max_zigzag)
        min_zagzig = min(x,min_zagzig)
        max_zagzig = max(y,max_zagzig)
    i += 1
if d[0] == "Zig-Zag" :
    print(min_zigzag, max_zigzag)
else : print(min_zagzig, max_zagzig)    
