from re import *
for n in range(10980,10**10,10980):
    if fullmatch(r'20[13579][13579]22[24680]*',str(n)):
        print(n,n//10980)