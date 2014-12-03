import time

c=0
for i in range(2,100):
    for j in range(1,10):
        if len(str(j**i))==i:
            print j,'^',i,'=',j**i
            c=c+1

print c
