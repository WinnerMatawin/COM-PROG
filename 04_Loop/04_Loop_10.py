import math
a = float(input())
l = 0
u = 0
q = a
while q != 0 :
    q = q//10
    u += 1
    
x = (l+u)/2
while abs(a-10**x) > (10**-10)*max(a, 10**x) :
    if 10**x > a :
        u = x
    if 10**x < a :
        l = x
    x = (l+u)/2
print(round(x,6))
    
