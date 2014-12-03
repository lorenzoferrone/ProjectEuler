import primes
import time

n=input("inserisci un numero: ")

t0=time.time()

lp=primes.listprimes(n)

lista=[]
maxim=0
val=0


for i in lp:
    c=1
    s=i
    for j in [x for x in lp if x>i]:
        s=s+j
        if (primes.isprime(s)!=0)and(s<=1000000):
            c=c+1
            lista.append(s) 
            #print s, lp[lp.index(i):lp.index(j)+1], len(lp[lp.index(i):lp.index(j)+1])
            if len(lp[lp.index(i):lp.index(j)+1])>maxim:
                maxim=len(lp[lp.index(i):lp.index(j)+1])
                val=s
                lista_r=lp[lp.index(i):lp.index(j)+1]

#print max([x for x in lista if x<1000000])
print val, maxim, lista_r
        
t1=time.time()
print t1-t0

    
    
    
    
