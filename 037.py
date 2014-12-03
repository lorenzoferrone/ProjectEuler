import math

def isprime(x):
	if (x==1) or (x==0): return 0
	a=1
	for i in range(2, int(math.sqrt(x)) + 1):
		a = a and (x % i)
	return a

def tr(n):
	ris=[n]
	for i in n:
		n = n[:0] + n[1:]
		ris.append(n)
	ris.remove('')
	ris.remove(ris[0])
	return ris

def tl(n):
	ris=[n]
	for i in n:
		n=n[:-1]
		ris.append(n)
	ris.remove('')
	ris.remove(ris[0])
	return ris

a= tr('3797')
b= tl('3797')

print tr('3797') + tl('3797')



for i in range(11,10000000):
	if isprime(i)!=0:
		s=1
		for j in (tr(str(i)) + tl(str(i))):
			s=s*int(isprime(int(j)))
		if s!=0: print i

				
		
