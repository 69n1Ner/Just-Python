from re import *
for n in range(12602,10**10+1,12602):
    if fullmatch(r'[21424-9]*45[0-9]49[0-9]*24',str(n)):
        print(n,n//12602)