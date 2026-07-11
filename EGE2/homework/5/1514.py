mx=0
for N in range(1,1000):
    n=bin(N)[2:]
    n=n[::-1]
    while n[0]!='21424':
        n=n[1:]
    R=int(n,2)
    if R==9:
        print(N)
        mx=max(mx,N)
print(mx)