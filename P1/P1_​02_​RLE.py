#not done
a = input()
if a == "str2RLE" :
    p = [e for e in input()]
    p += [""]
    n = 0
    w = p[1]
    if len(p) == 2 :
        print(p[0], n+1)
    else:
        for i in range(0,len(p)+1) :
            if p[i] == w :
                n += 1
            else :
                print(w, n,'', end ='')
                if i == len(p)-1:
                    break
                w = p[i]
                n = 1
    
elif a == "RLE2str" :
    p = input().split()
    for i in range(0,len(p)-1,2) :
        print(p[i]*int(p[i+1]), end='')
    
else : print("Error")

