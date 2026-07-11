def f(n):
    s=set()
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            s|={d,n//d}
    return sorted(s)

for n in range(1204300,1204380+1):
    d=[i for i in f(n) if i%2==0]
    sm=sum(d)
    if sm>0 and sm%10==0:
        print(n,sm)