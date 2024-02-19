u = input()
v = input()
u_real = list(map(float,u[1:-1].split(",")))
v_real = list(map(float,v[1:-1].split(",")))
x = [0,0,0]

for i in range(3) :
    x[i] = u_real[i] + v_real[i]
print(str(u_real) , "+" , str(v_real) , "=" , str(x))