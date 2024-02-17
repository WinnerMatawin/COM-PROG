# Roots of ax^2+bx+c=0

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    r = -c / b
    print(round(r,3))
else:
    t = ((b**2)-(4*a*c))**0.5 
    r1 = (-b-t)/(2*a)
    r2 = (-b+t)/(2*a)
    print(round(r1,3),round(r2,3))




