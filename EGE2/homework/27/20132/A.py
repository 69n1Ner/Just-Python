f=open('27A_1_20132.txt')
data=[]
for l in f:
    x,y=list(map(float,l.replace(',','.').split()))
    data.append([x,y])
from math import dist
clusters=[]
while data:
    cl=[data.pop()]
    for point in cl:
        for p1 in data:
            if dist(point,p1)<5:
                cl.append(p1)
                data.remove(p1)
    clusters.append(cl)
print([len(cl) for cl in clusters])

def center(cl):
    mas=[]
    for point in cl:
        sm=0
        for p1 in cl:
            sm+=dist(point,p1)
        mas.append([sm,point])
    return max(mas)[1] ###
centers=[center(cl) for cl in clusters]
print(centers)
px=sum(x for x,y in centers)/len(centers)
py=sum(y for x,y in centers)/len(centers)
print(int(px*10000),int(py*10000))
