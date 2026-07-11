file=open('27_B_21599.txt')
# clusters=[[] for x in range(6)]
clus=[]
from math import dist
def f(x):
    return x-10
data=[]
for line in file:
    x,y=map(float,line.replace(',','.').split())
    data.append([x,y])
while data:
    cl=[data.pop()]
    for p1 in cl:
        for p2 in data:
            if dist(p1,p2)<1.5:
                cl.append(p2)
                data.remove(p2)
    clus.append(cl)
print([len(cl) for cl in clus])
def center(cl):
    mas=[]
    for p1 in cl:
        sm=0
        for p2 in cl:
            sm+=dist(p1,p2)
        mas.append([sm,p1])
    return min(mas)[1]
centers=[center(cl) for cl in clus]
print(centers)
px=sum(x for x,y in centers)/len(centers)
py=sum(y for x,y in centers)/len(centers)
print(abs(int(px*10000)),abs(int(py*10000)))