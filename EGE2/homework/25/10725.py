from re import *
N=65_001
while True:
    if fullmatch(r'6[0-9]*97[0-9]*5[0-9]',str(N)):
        dels = []
        if N%2==0:
            dels.append(N)
        for d in range(2,N//2+1):
            if N%d==0 and d%2==0:
                dels.append(d)
        if len(dels)>=4:
            print(N,sum(dels))
    N+=1