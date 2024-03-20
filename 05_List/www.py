f = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
ni = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy', 'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']
n = int(input())
for i in range(n) :
    w = input()
    if w in f:
        print(ni[f.index(w)])
    elif w in ni :
        print(f[ni.index(w)])
    else: print('Not found')