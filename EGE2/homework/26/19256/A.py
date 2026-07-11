f=open('26_19256.txt')
N=int(f.readline())
data=set()
for l in f:
    ida,n=map(int,l.split())
    data.add((ida,n))
data=list(sorted(data))

lst=[[] for x in range(60_000)]
for i in range(0,len(data)):
    lst[data[i][0]].append(data[i][1])
mx=0
co=[0]*60_000
for el in lst:
    if len(el)>2:
        fl=True
        for i in range(1,len(el)):
            if el[i]-el[i-1]!=1:
                fl=False
        if fl:
            co[lst.index(el)]=len(el)
for el in co:
    if el==max(co):
        print(co.index(el),el)
        break
