def rev(n):
	a=str(n)
	a=a[::-1]
	return int(a)

def b(n, digits=8):
	return int("{0:0>{1}}".format(bin(n)[2:], digits))



s=0
for i in range(1,1000000,2):
	if (i==rev(i)) and (b(i) == rev(b(i))):
		print i
		s=s+i

print s
