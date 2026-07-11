from re import *
for n in range(4013,10**12,4013):
    if fullmatch(r'123[0-9]4[0-9]*5679',str(n)):
        print(n,n//4013)
        if str(n)[0]=='2':
            break