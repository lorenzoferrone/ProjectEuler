import math

def score(w):
	s=0
	for i in w:
		s=s+(ord(i)-64)
	return s

def tr(x):
	if (int(math.sqrt((x*8+1)))**2==(x*8+1)):
		return 1
	else: return 0
	
s=0

f=open("words.txt")
l = f.readlines()
for i in l:
	t=i.split(",")

for i in t:
	if tr(score(i))==1:
		s=s+1

print s


