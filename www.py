def reverse(d) :
    r = {}
    for k in d :
        v = d[k]
        r[v] = k
    return r

def keys(d, v) :
    r = []
    for k in d :
        if d[k] == v :
            r.append(k)
    return r

exec(input().strip())