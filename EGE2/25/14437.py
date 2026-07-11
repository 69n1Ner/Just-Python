def delit(n):
    s=set()
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            s|={d,n//d}
    return sorted(s)
for n in range(700_000-1,0,-1):
    d=delit(n)
    m=(sum(d)/(len(d) or 1))//1
    if m%1000==313:
        print(n,int(m))