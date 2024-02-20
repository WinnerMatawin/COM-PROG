sum = 0
n = 0
x = float()
while True :
    x = input()
    if x == "q":
        break
    sum += float(x)
    n += 1
if n == 0 :
    print("No Data")
else :print(round((sum/n),2))
    
