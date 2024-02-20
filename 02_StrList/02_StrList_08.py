import math

a,b,c = input().split(",")
nb = len(b)
nc = len(c)
n = int(a+b+c) - int(a+b)
d = 10**(nb+nc) - 10**nb
g = math.gcd(n, d)
print(n//g, '/', d//g)
    
    
