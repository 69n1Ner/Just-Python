for N in range(248015,251575+1,2):
    for d in range(2,int(N**0.5)+1):
        if N%d==0 and d==N**0.5:
            print(N,d)