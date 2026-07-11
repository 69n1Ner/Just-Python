def dels(n):
    s=set()
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            s|={d,n//d}
    return sorted(list(s))

def s(n):
    dls=dels(n)
    if len(dls)<3:
        return 0
    return sum(dls[-3:])
N=10_000_001
while True:
    if s(N)**0.5==int(s(N)**0.5) and s(N)!=0:
        print(s(N))

    N+=1