import primes
import time

def factor(n,l):
    a=set()
    div=2
    if n in l:
        a.add(n)
        return a
    while (n not in l):
        if n%div==0: 
            n=n/div
            a.add(div)
            div=div-1
        div=div+1
    a.add(n)
    return a

tp=time.time()
l=primes.listprimes(100000)
tp1=time.time()
print tp1-tp
#x=input("inserisci un numero: ")
#print factor(x,l), len(factor(x,l))

for i in range(30000,100000):
   if (len(factor(i,l))==4):
       if (len(factor(i+1,l))==4):
           if (len(factor(i+2,l))==4):
               #print i, factor(i,l)
               #break
               if (len(factor(i+3,l))==4):
                    print i, factor(i,l)
                    break

t1=time.time()

print t1-tp
