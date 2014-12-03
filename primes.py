def isprime(x):
    if x == 2 or x == 3: 
        return True
    for i in range(2, int(x**(0.5)) + 2):
        if x % i == 0: 
            return False
	
    return True

def listprimes(n):
    l=filter(isprime, range(2,n))
    return l

def lastprime(n):
    a=listprimes(n)    
    return a[len(a)-1]


