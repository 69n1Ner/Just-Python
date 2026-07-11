f=open('27_B_21720.txt')
clusters=[[],[],[]]
for l in f:
    x,y=list(map(float,l.split()))
    if y>-2:
        clusters[0].append([x,y])
    if y<-2:
        clusters[1].append([x,y])
from math import *


print([len(cl) for cl in clusters])
#28603 10294
def center(cl):
    mas=[]
    for point in cl:
        sm=0
        for p1 in cl:
            sm+=dist(point,p1)
        mas.append([sm,point])
    return min(mas)[1]

centers=[center(cl) for cl in clusters]
print(centers)

px=sum(x for x,y in centers)/len(centers)
py=sum(y for x,y in centers)/len(centers)

print(abs(int(px*10000)),abs(int(py*10000)))


