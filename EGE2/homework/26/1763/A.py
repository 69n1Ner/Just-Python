f=open('test.txt')
N,M=map(int,f.readline().split())
data=[]
for l in f:
    data.append(int(l))
data.sort(key=lambda x:-x)
k=0
while True:
    sm=0
    l=M
    i=0
    first=data[0]
    data.remove(first)
    lst=[]
    for el in data[1:]:
        if first+el>=M:
            lst.append(el)
            data.remove(el)
    for el in lst:
        if first+el<M:
            first+=el
        else:
            mn=min(lst)
    data.append((first+mn)-M)
    k+=1
print(data)