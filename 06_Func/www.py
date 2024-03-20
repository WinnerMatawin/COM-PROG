def make_int_list(x):
    return [int(e) for e in x.split()]

def is_odd(e):
    if e%2 != 0:
        return True
    return False

def odd_list(alist):
    mylist = []
    for e in alist :
        if e %2 != 0 :
            mylist.append(e)
    return mylist

def sum_square(alist):
    return sum([e**2 for e in alist])


exec(input().strip())