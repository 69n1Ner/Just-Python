f=open('../../files/2035.txt')
k=0
for l in f:
    line=l.split()
    if sum(map(int,line))==180:
        k+=1
print(k)