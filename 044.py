def penta(x):
    return [n*(3*n-1)/2 for n in range(1,x)]

def isq(x):
    r = x**0.5
    if int(r)==r:
        return True
    return False
        


def uno(p,k):
    a = p**2
    b = k**2
    return 1 + 18*b + 18*a -6*k -6*p

def due(p,k):
    a = p**2
    b = k**2
    return 1 - 18*b + 18*a +6*k -6*p


for p in range(1,1000):
    for k in range(1,p):
        if isq(uno(p,k)):
            if isq(due(p,k)):
                print p,k
        
