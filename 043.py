from __future__ import division  
import math 
import itertools
import time


def subd(n):
    primes_list=[2,3,5,7,11,13,17]
    a=1
    s=str(n)
    for i in range(1,8):
        if ((int(s[i:i+3])) % (primes_list[i-1]) == 0):
            pass
        else:
            a=0 
            break
    return a
    


a = itertools.permutations(range(10))
t0=time.time()
b=[i for i in a if (i[0]!=0 and i[3]%2==0 and i[5]%5==0)]

sum=0

for j in b:
    s=""
    for i in j:
        s=s+str(i)
    num=int(s)
    if subd(num)==1:
        print num
        sum=sum+num

print sum

t1=time.time()

print t1-t0


