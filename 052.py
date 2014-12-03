import time

def sd(l):
    s=[]
    for i in l:
        s.append(str(i))
    for i in s:
        if (len(i)!= len(s[0])): return 0
    for c in s[0]:
        for j in s:
            if c in j: 
                pass
            else: return 0
    
    return 1

for i in range(1,1000000):
    if sd([i,2*i,3*i,4*i,5*i,6*i])==1:
        print i,2*i,3*i,4*i,5*i,6*i

