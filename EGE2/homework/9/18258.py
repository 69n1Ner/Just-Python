f=open('../../files/18258.txt')
k=0
for line in f:
    k+=1
    l=line.split()
    if sorted(l)==l:
        if len(set(l))==len(l):
           if sum(map(int,l))%2==0:
               print(k)