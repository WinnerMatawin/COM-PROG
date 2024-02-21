#not checked
result = [e for e in input()]
target = int(input())
comb = []
i = 0
total = 0
num = "0123456789"

for f in range(1,11) :
    scoref = 0
    if f == 10 :
        if result[i+1] in "/" :
            comb += [result[i]] + [result[i+1]] + [result[i+2]]

        if result[i] == "X" :
            comb += [result[i]] + [result[i+1]] + [result[i+2]]
        
        else :
            comb += [result[i]] + [result[i+1]]

    else:
        if result[i] == "X" :
            comb += [result[i]] + [result[i+1]] + [result[i+2]]
            i += 1
        elif result[i] in num :
            if result[i+1] in num:
                comb += [result[i]] + [result[i+1]]
            else:
                comb += [result[i]] + [result[i+1]] + [result[i+2]]
            i += 2
        
        
    for e in range(len(comb)) :
        if comb[e] in num :
            scoref += int(comb[e])
        if comb[e] == "X" :
            scoref += 10
        if comb[e] == "/" :
            scoref += 10-int(comb[e-1])
    comb = []
    total += scoref
    if target == f :
        print(scoref)

if target not in range(1,11) :
    print(total)
