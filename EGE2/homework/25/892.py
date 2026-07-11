def dels(n):
    s=set()
    for d in range(2,int(n**0.5)+1):
        if n%d==0 and d*d==n:
            return set()
            break
        if n%d==0:
            s|={d,n//d}
    return sorted(s)

for n in range(154026,154043+1):
    if len(dels(n))==2:
        print(dels(n)[-1],n)
