def rev(n):
    n=list(str(n))
    n.reverse()
    a=0
    l=len(n)
    for i in range(l):
        a=a+10**(l-i-1)*int(n[i])
    return a

def anr(n):
    return n+rev(n)
    
def isp(n):
    return n==rev(n)
    
def f(n):
    for i in range(50):
        n=anr(n)
        if isp(n): return n
    return -1

def cl():
    c=0
    for i in range(10000):
       if f(i) == -1:
           print i
           c=c+1
    return c
    

a=int(raw_input('inserisci numeri: '))
#print anr(a)
#print isp(a)
print f(a)
print cl()
