def dels(n):
    s=set()
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            s|={d,n//d}
    return sorted(s)
k=0
N=136_180
while True:
    ds=dels(N)
    if sum(ds)%385==91:
        print(N,sum(ds))
        k+=1
    N+=1
    if k==4:
        break
