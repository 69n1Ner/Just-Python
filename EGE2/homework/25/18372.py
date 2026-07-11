def dels(n):
    s=set()
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            s|={d,n//d}
    s|={1}
    return sorted(s)
print(dels(10))
for n in range(770_000-1,0,-1):
    D=dels(n)
    A=(sum(D)/len(D))//1
    if A%100==12:
        print(n,int(A))
