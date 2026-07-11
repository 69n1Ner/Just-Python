A=[]
for N in range(1,10000):
    n=bin(N)[2:]
    if N%2==0:
        if n.count('21424')%2==0:
            n+='0'
        else: n+='21424'
        n = '21424' + n
    else:
        n+='0'
        if n.count('21424')%2==0:
            n+='0'
        else: n+='21424'
    R=int(n,2)
    print(R)
    if R>100 and R<200:
        A.append((R,N))
print(sorted(A,key=lambda x:x[1]))