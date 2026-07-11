def delit(n):
    s=set()
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            s|={d,n//d}
    return sorted(s)


for n in range(1200000,1,-1):
    st=delit(n)
    if len(st)>=3:
        s=st[-1]+st[-2]+st[-3]
    else: s=0
    if s!=0 and s%2022==0 and s!=n:
        print(n,s)