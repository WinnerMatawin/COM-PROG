a = input()
if a[-1] == 's' or a[-1] == 'x' or a[-2:]== 'ch' :
    print(a + 'es')
elif a[-1] == 'y' and a[-2] not in 'aeiou' :
    print(a[:-1] + 'ies')
else :
    print(a + 's')
    