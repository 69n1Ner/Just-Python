f=open('27A_18055.txt')
data=[]
for l in f:
    x,y,h=list(map(float,l.split()))
    if 200<x<305 and 200<y<305:
        pass
    else:
        data.append([[x,y],h])

from math import *
clusters=[]
while data:
    cl=[data.pop()]
    for point in cl:
        for p1 in data:
            if dist(point[0],p1[0])<55:
                cl.append(p1)
                data.remove(p1)
    clusters.append(cl)
print([len(cl) for cl in clusters])

def center(cl):
    mas=[]
    for point in cl:
        sm=0
        for p1 in cl:
            sm+=dist(point[0],p1[0])*p1[1]
        mas.append([sm,point[0]])
    return min(mas)[1]

centers=[center(cl) for cl in clusters]

px=sum(x for x,y in centers)/len(centers)
py=sum(y for x,y in centers)/len(centers)
print(int(px*100000),int(py*100000))