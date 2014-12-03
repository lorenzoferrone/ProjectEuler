from __future__ import division
import random
import time

N=100000000

def peter():
    s=0
    for i in range(9):
        t=random.randint(1,4)
        s=s+t
    return s
    
def colin():
    s=0
    for i in range(6):
        t=random.randint(1,6)
        s=s+t
    return s



pv=0
cv=0

t0=time.time()


for i in range(N):
    p=peter()
    c=colin()
    if p==c: pass
    if p > c: pv=pv+1
    else: cv=cv+1

t1=time.time()
print pv, cv, pv/N, cv/N
print t1 - t0
