for N in range(1,1000000):

    n=bin(N)[2:]
    if n.count('1')%2==0:
        n='10'+n[2:]+'0'
    else:
        n='11'+n[2:]+'1'
    R=int(n,2)
    if R>171:
        print(N)
        break