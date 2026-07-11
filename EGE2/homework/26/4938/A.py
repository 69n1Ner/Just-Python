f=open('26_4938.txt')
L,N=map(int,f.readline().split())
prom=[]

for l in f:
    start,end =map(int,l.split())
    prom.append([start,end])
prom.sort(key=lambda x:(x[1],x[0]))
con=0
k=0
mn=0

for el in prom:
    if con<=el[0]:
        con=el[1]
        mn=el[0]
        k+=1
print(k,mn)
