n=250_201
while True:
    dels=[]
    for d in range(2,n//2+1):
        if n%d==0:
            dels.append(d)
    if len(dels)==0:
        n+=1
        continue
    if (max(dels)+min(dels))%123==17:
        print(n,max(dels)+min(dels))
    n+=1