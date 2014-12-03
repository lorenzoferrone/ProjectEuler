import itertools
import time
import primes

def perm(n):
    l=[n]
    a=itertools.permutations(list(str(n)))
    for i in a:
        if int("".join(list(i))) not in l:
            l.append(int("".join(list(i))))
    return l
    
l=[x for x in primes.listprimes(10000) if x >1000]



lp=[] #lista delle permutazioni, una lista di liste
sc=[] #primi da scartare
for i in l:
    if i in sc: continue 
    p=[i] #lista delle permutazioni che sono numeri primi, listate una sola volta
    for j in perm(i):
        if (j in l) and (j not in p):
            p.append(j)
            sc.append(j)
    if len(p)>=2:
        lp.append(p)

c=0
#for i in lp:
    #if len(i)>=3:
        #print i
        #c=c+1

#print c

t0=time.time()

for i in lp:
    if len(i)>=3:
        for j in i:
            for k in range(2,5000):
                if (j+k in i) and (j+2*k in i):
                    print j, j+k,j+2*k, k
                
t1=time.time()

print t1-t0
        


