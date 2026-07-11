f=open('../../files/2098.txt')
k=0
for line in f:
    l=list(map(int,line.split()))
    if (l[0]==0 or l[1]==0) and (l[2]==0 or l[3]==0):
        k+=1
print(k)