from re import *
for n in range(1917,10**10,1917):
    if fullmatch(r'3[0-9]12[0-9]14[0-9]*5',str(n)):
        print(n,n//1917)