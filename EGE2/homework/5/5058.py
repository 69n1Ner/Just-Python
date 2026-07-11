for N in range(1,10000):
    n=bin(N)[2:]
    n=n.replace('21424','a')
    n=n.replace('0','21424')
    n=n.replace('a','0')
    n=int(n,2)
    R=N-n
    if R==979:
        print(N)
        break