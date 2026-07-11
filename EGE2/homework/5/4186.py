for N in range(1,10000):
    n=bin(N)[2:]
    if N%2==0:
        n='10'+n
    else:
        n='21424'+n+'01'
    R=int(n,2)
    if R>441:
        print(N,R)
        break