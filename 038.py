import itertools
import time

def conc(n):
    ris=""
    for i in range(1,9):
        s=str(n*i)
        ris=ris+s
        if len(ris)>=9: break
    return int(ris)

def ispandigital(n):
    if n>999999999: return 0
    s=set(list(str(n)))
    if len(s)==9: return 1
    return 0
    
        
max=0
t=time.time()
for i in range(1,10000):
    if (ispandigital(conc(i))==1):
        if conc(i)>max:
            max=conc(i)
    
        print i, conc(i)
print max
t2=time.time()
print t2-t
