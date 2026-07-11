from collections import Counter
f=open('../../files/20899.txt')
k=0
for line in f:
    l=list(map(int,line.split()))
    mx=max(l)
    sm=sum(l)-mx
    if mx < sm:
        if sorted(Counter(line.split()).values()) == [1,1,2]:
            k+=1
print(k)