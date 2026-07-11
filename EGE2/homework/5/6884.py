A=[]
for N in range(1,10000):
    n=bin(N)[2:]
    if N%2==0:
        n='21424'+n+'0'
    else:
        n='11'+n+'11'
    R=int(n,2)
    if R>225:
        A.append(R)
print(min(A))