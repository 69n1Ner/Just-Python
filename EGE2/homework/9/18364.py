from collections import Counter
k=0
f=open('../../files/18364.txt')
for line in f:
    l=list(map(int,line.split()))
    t = Counter(l)
    s1=0
    s2=1
    if len(Counter(l))<7:
        for el in t.keys():
            if t[el]>1:
                s2*=el**t[el]
            else:
                s1+=el
        if (3*s1)<=s2:
            k+=1
print(k)