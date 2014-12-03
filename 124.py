def factor(n):
    f=[]
    c=0
    i=2
    while (i<2*n):
        while (n%i == 0):
            #f.append(i)
            n=n/i
            c=c+1
        if c!=0: f.append([i,c])
        i=i+1
        c=0
    return f
    
def rad(n):
    a=1
    for i in factor(n):
       a=a*i[0]
    return a


a = int(raw_input('inserisci numero: '))
#b = int(raw_input('inserisci numero: '))
l=[]
for i in range(1,100001):
    l.append([i,rad(i)])
l.sort(key=lambda x: x[1])
    

#print factor(a)
#print rad(a)
#print l
print l[(a-1)][0]
