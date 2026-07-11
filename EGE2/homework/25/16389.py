from re import *
for n in range(98591,10**10+1,98591):
    if fullmatch(r'5[0-9]2[0-9]*3[0-9]3[0-9]',str(n)):
        print(n,n//98591)