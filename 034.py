def p(x,y): return x*y
def fact(n):
	if n==0: return 1
	if n==1: return 1 
	return reduce(p, range(2,n+1))

def f(n):
	s=0
	for i in str(n):
		s=s+fact(int(i))
	return int(s)

	
s=0
for i in range(3,2540159):
		if i == f(i):
			print i
			s=s+i

print "\n", s
