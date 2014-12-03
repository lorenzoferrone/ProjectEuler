import time

def seq(x):
    l=[]
    for n in range(1,x+1):
        l.append(n**10-n**9+n**8-n**7+n**6-n**5+n**4-n**3+n**2-n+1)
    return l

print seq(11)
