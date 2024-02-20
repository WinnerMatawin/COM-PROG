a = input().split()
b = input().split()
a[1] = float(a[1])
b[1] = float(b[1])

r1a = False
r1b = False
r2a = False
r2b = False
r3a = False
r3b = False
r4a = False
r4b = False

if a[2] == "A" and (a[3] <= "C" and a[4] <= "C") : r1a = True
if b[2] == "A" and (b[3] <= "C" and b[4] <= "C") : r1b = True

if (a[1] == b[1]) : r2a = r2b = True
if (a[1] > b[1]) : r2a = True
if (a[1] < b[1]) : r2b = True
if (a[3] == b[3]) : r3a = r3b = True
if (a[3] < b[3]) : r3a = True
if (a[3] > b[3]) : r3b = True
if (a[4] == b[4]) : r4a = r4b = True
if (a[4] < b[4]) : r4a = True
if (a[4] > b[4]) : r4b = True

if r1a and r1b == True :
    if (r2a and r2b == True) :
        if r3a and r3b == True :
            if (r4a and r4b == True) : print("Both")
            else :
                if r4a == True: print(a[0])
                else: print(b[0])
        elif r3a == True: print(a[0])
        else: print(b[0])
    elif r2a == True: print(a[0])
    else: print(b[0])
elif r1a == True : print(a[0])
elif r1b == True : print(b[0])
else : print("None")