import math



max_len = 0
max_p = 12
for p in range(12,1000):
    lati = [[a,b,p-a-b] for a in range(1,p) for b in range(1,a) if 2*(a*p + p*b -a*b)==p**2]
    l = len(lati)
    if l > max_len:
        max_len = l
        max_p = p
        max_lati = lati

print max_len, max_p, max_lati