a = int(input())
n = list(map(int, str(a)))
s = list(str(a))
n12 = (11-((13*n[0] + 12*n[1] + 11*n[2] + 10*n[3]
        + 9*n[4] + 8*n[5] + 7*n[6] + 6*n[7] + 5*n[8]
           + 4*n[9] + 3*n[10] + 2*n[11])%11))%10
print(s[0], s[1]+s[2]+s[3]+s[4],s[5]+s[6]+s[7]+s[8]+s[9],
    s[10]+s[11], n12)
