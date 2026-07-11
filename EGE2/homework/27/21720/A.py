f=open('27_A_21720.txt')
f.readline()
clusters=[[],[]]
for l in f:
    x,y=map(float,l.replace(',','.').split())
    if y>-2:
        clusters[1].append([x,y])
    if y<-2:
        clusters[0].append([x,y])
from math import dist

print([len(cl) for cl in clusters])

def center(cl):
    mas=[]
    for p1 in cl:
        sm=0
        for p2 in cl:
            sm+=dist(p1,p2)
        mas.append([sm,p1])
    return min(mas)[1]
centers=[center(cl) for cl in clusters]
print(centers)
px=sum(x for x,y in centers)/len(centers)
py=sum(y for x,y in centers)/len(centers)
print(abs(int(px*10000)),abs(int(py*10000)))