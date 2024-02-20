s = input()
a = input()
c = 0
if len(s) != len(a) :
    print("Incomplete answer")
else :
    for i in range(len(s)) :
        if s[i] == a[i] :
            c += 1
    print(c)

    