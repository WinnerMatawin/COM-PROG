l = 'abcdefghijklmnopqrstuvwxyz'
u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = ''
x = input()
while x != 'end' :
    for i in x :
        if i in l :
            a += l[(l.index(i)+13)%26]
        elif i in u :
            a += u[(u.index(i)+13)%26]
        else:
            a += i
    print(a)
    a = ''
    x = input()       

            
        