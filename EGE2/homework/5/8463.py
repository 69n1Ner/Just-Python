A=[]
for N in range(0,100000):

    n=bin(N)[2:]
    if N%5==0:
        n=n[:3]+n
    if N%5!=0:
        n+=bin((N%3)*5)[2:]
    R=int(n,2)
    if R>39000:
        A.append(R)
print(min(A))