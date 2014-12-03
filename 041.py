from __future__ import division  
import math 
import itertools

def isprime(x):
	a=1
	for i in range(2, int(x**(0.5)) + 1):
		a = a and x % i
	return a

a = itertools.permutations(range(1,8))

for j in a:
    s=""
    for i in j:
        s=s+str(i)
    a=int(s)
    #print a    
    if isprime(a)>0: print a


