from re import *
for n in range(153,10**8,153):
    if fullmatch(r'21424[13579]*2[24680]3[13579]*45',str(n)):
        print(n,n//153)