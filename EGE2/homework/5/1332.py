for N in range(1,10000):
    n=bin(N)[2:]
    t=n[0]
    n = n[1:]
    n=n.replace('1','a')
    n=n.replace('0','1')
    n=t+n.replace('a','0')
    r=int(n,2)
    R=r+N
    if R>99:
        print(N)