n=700_001
while True:
    dels=[]
    for d in range(2,n//2+1):
        if n%d==0:
            dels.append(d)
    m=0
    if len(dels)>=2:
        m=max(dels)+min(dels)
    if m%10==8:
        print(n,m)
    n+=1