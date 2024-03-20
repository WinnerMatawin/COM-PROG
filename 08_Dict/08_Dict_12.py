name = {}
for k in range(int(input())):
    n1, n2 = input().split()
    name[n1] = n2
    name[n2] = n1
for k in range(int(input())) :
    q = input()
    if q in name :
        print(name[q])
    else:
        print('Not found')
    
