def isprime(x):
	a=1
	for i in range(2, int(x**(0.5)) + 1):
		a = a and (x % i)
	return a


def rot(n):
    n=str(n)
    r=[]
    for i in range(len(n)):
       r.append(int(n[i:]+n[:i]))
    return r

def cp(n):
    for i in rot(n):
        if isprime(i) == 0: return False
    return True
    
#a=int(raw_input('inserisci numero: '))
#print rot(a)
#print isprime(a)
#print cp(a)
c=0
for i in range(2,1000000):
   if cp(i)==True:
       c=c+1
       print i

print '\n', c
