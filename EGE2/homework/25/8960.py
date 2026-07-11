from re import *
N=500_001
while True:
    dels=[1,N]
    for d in range(2,N//2+1):
        if N%d==0:
            dels.append(d)
    ds=str(sum(dels))
    if fullmatch(r'[0-9]*7[0-9]',ds):
        print(N,ds)

    N+=1