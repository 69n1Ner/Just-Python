f=open('../../files/21704.txt')
for line in f:
    l=list(map(int,line.split()))
    if sorted(l,reverse=True)==l:
        mx=max(l)
        mn=min(l)
        sr1=(mx+mn)/2
        sr2=(sum(l)-mx-mn)/5
        if sr1>sr2:
            print(sum(l))
            break
