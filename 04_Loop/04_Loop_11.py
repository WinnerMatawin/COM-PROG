s = input()
c = 0
let = s[0]
for i in range(len(s)) :
    if s[i] != let :
        print(let, c, end=' ' )
        c = 0
    let = s[i]
    c += 1
    if i == len(s)-1 :
        print(let, c)
        

