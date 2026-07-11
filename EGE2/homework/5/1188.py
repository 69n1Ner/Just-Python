for N in range(1,10000):
    n=bin(N)[2:]
    if N%2==0:
        n+=n[-2:]
    else:
        n='21424'+n+'21424'
    R=int(n,2)
    if R>130:
        print(R)
