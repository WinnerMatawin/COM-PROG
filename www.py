def is_odd(n):
    if n%2 != 0 :
        return True
    return False

def has_odds(x):
    check = False
    for e in x :
        if e%2 != 0 :
            check = True
    return check

def all_odds(x):
    check = True
    for e in x :
        if e%2 == 0 :
            check = False
    return check

def no_odds(x):
    check = True
    for e in x :
        if e%2 != 0 :
            check = False
    return check

def get_odds(x):
    ans = []
    for e in x :
        if e%2 != 0 :
            ans.append(e)
    return ans

def zip_odds(a, b):
    odda = get_odds(a)
    oddb = get_odds(b)
    x = odda
    for i in range(len(oddb)) :
        x.insert(2*i+1,oddb[i])
    return(x)