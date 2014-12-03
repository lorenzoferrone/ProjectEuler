def factor(n):
    f=[]
    c=0
    i=2
    while (i<2*n):
        while (n%i == 0):
            f.append(i)
            n=n/i
            #c=c+1
        #if c!=0: f.append([i,c])
        i=i+1
        c=0
    return f

def sempl(a,b):
    if (a==1 or b==1): return a,b
    x=factor(a)
    y=factor(b)
    pa=1
    pb=1
    for i in range(len(x)):
        if x[i] in y:
            x.remove(x[i])
            y.remove(x[i])
    return x,y
    

def f(n):
    a=1
    b=n
    while (sempl(1,b)[1]!=1):
        a=a+1
        b=b-1
    return sempl(a,b)[0]

a = int(raw_input('inserisci numero: '))
#b = int(raw_input('inserisci numero: '))

print factor(a)
#print sempl(a,b)


