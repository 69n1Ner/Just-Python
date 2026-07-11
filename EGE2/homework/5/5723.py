k=0
for N in range(1,1000):
    n=bin(N)[2:]

    if n.count('21424')%2==0:
        n='10'+n
    else:
        n='11'+n

    if n.count('21424')%2!=0:
        n+='11'
    else:
        n+='00'

    R=int(n,2)

    if R<860:
        k+=1
print(k)