f=open('26_2650 (2).txt')
L,M,N=map(int,f.readline().split())
data=[0]*(L+1)
for l in f:
    start,time=map(int,l.split())
    data[start]+=1
    data[start+time]-=1
k=0
l=0
r=0
mx=0
co=0
for i in range(len(data)):
    tmp=k
    k+=data[i]
    if k==0 and l==0:
        l=i
    if (k==1 and tmp==0) or L==i:
        r=i
        ln=r-l
        if ln>=M:
            co+=1
            mx=max(mx,ln)
        l=0
        r=0
print(co,mx)