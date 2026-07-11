f=open('27.6.A_20290.txt')
data=[]
for l in f:
    x,y=map(float,l.split())
    data.append([x,y])
from math import dist
clusters=[]
while data:
    cl=[data.pop()]
    for p1 in cl:
        for p2 in data:
            if dist(p1,p2)<0.5:
                cl.append(p2)
                data.remove(p2)
    clusters.append(cl)
print([len(cl) for cl in clusters])
del clusters[-1]
def edge(cl):
    mas=[]
    for p1 in cl:
        sm=0
        for p2 in cl:
            sm+=dist(p1,p2)
        mas.append([sm,p1])
    return max(mas)[1]
edges=[edge(cl) for cl in clusters]
tx=sum(x for x,y in edges)/len(edges)
ty=sum(y for x,y in edges)/len(edges)
print(abs(int(tx*10_000)),abs(int(ty*10_000)))