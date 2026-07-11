from re import *
for n in range(1984,10**10,1984):
    if fullmatch(r'[2468]9[0-9]23[0-9][0-9]*23[13579][02468]',str(n)):
        print(n,n//1984)