a,b,c,d = list(map(int,input().split()))
if a > b :
    a,b = b,a
    if d >= a :
        if c >d :
            c -= a
    else :
         c += a
    b = a + c + d
else :
    if c > a >= b :
        d += a
    if d > c :
        b += 2
    else :
        b *= 2
print(a, b, c, d)
