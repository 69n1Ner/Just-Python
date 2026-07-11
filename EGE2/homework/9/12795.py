f=open('../../files/12795.txt')
k=0
for line in f:
    l=list(map(int,line.split()))
    sr=sum(l)//len(l)
    if sr in l:
        k+=1
print(k)