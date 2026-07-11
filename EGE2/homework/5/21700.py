A=[]
for N in range(3,1000):
    s=''
    n=N
    while n:
        s=str(n%3)+s
        n//=3
    if N%3==0:
        s+=s[-3:]
    else:
        f=int(N)%3*3
        g=''
        while f:
            g = str(f % 3) + g
            f //= 3
        s+=g
    r=int(s,3)
    print(N,r)
    if r<=150:
        A.append(N)
print(max(A))