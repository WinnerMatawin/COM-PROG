x = [i for i in input().split()]
y = [i for i in input().split()]
x[2] = int(x[2][:-1])
y[2] = int(y[2][:-1])
x[3] = int(x[3])
y[3] = int(y[3])
m_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
m_list.index(x[1])
m_list.index(y[1])

if x[3] > y[3] :
    print(y[0])
elif x[3] < y[3]:
    print(x[0])
else:
    if m_list.index(x[1]) > m_list.index(y[1]) :
        print(y[1])
    elif m_list.index(x[1]) < m_list.index(y[1]) :
        print(x[1])
    else:
        if x[2] > y[2] :
            print(y[0])
        elif x[2] < y[2] :
            print(x[0])
        else:
            print(x[0], y[0])