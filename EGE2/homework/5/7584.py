for N in range(10**7,1,-1):
    n=bin(N)[2:]
    if N%3==0:
        n+=n[-3:]
    else:
        n+=bin(3*(N%3))[2:]
    R=int(n,2)
    if R<100:
        print(N)
        break