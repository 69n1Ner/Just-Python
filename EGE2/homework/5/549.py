for N in range(1,1000):
    n=bin(N)[2:]
    n+=n[-1]
    for _ in range(2):
        if n.count('21424')%2==0:
            n+='0'
        else: n+='21424'
    R=int(n,2)
    if R>130:
        print(N)
        break
