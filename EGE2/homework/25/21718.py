from re import *
reg=r'4[0-9]*4736[0-9]*1'
for n in range(7993,10**10,7993):
    if fullmatch(reg,str(n)):
        print(n,n//7993)
