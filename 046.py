import primes

N = 1000000
ll = set()
quad = set()

def check(n):
    global ll
    global quad
    sp = set(primes.listprimes(n))
    ll = ll.union(sp)
    qq = [2*x**2 for x in range(n)]
    quad = quad.union(qq)
    for i in ll:
         for j in qq:
             if i+j == n:
                 #print i, j
                 return True
    
    return False
    

for i in range(5,N,2):
    if check(i) == False:
        print i



    