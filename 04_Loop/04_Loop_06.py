h = int(input())
p = h-2
q = 1
print("."*(h-1) + "*")
for i in range(h-2) :
    print("."*p + "*" + "."*q+"*")
    p -= 1
    q += 2
print("*"*(2*h-1))
