n = input()
if len(n) < 4 :
    ans = n
    d = ''
if len(n) == 4 :
    ans = round(float(n)/1000,1)
    d = "K"
elif 4 < len(n) < 7 :
    ans = round(float(n)/1000)
    d = "K"
elif len(n) == 7 :
    ans = round(float(n)/1000000,1)
    d = "M"
elif 7 < len(n) < 10 :
    ans = round(float(n)/1000000)
    d = "M"
elif len(n) == 10 :
    ans = round(float(n)/1000000000,1)
    d = "B"
elif 10 < len(n) :
    ans = round(float(n)/1000000000)
    d = "B"
print(str(ans)+d)
