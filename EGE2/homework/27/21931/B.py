f=open('27_B_21931.txt')
data=[]
for l in f:
    x,y=map(float,l.replace(',','.').split())
    data.append([x,y])
clusters=[]
from math import dist
while data:
    cl=[data.pop()]
    for p1 in cl:
        for p2 in data:
            if dist(p1,p2)<0.9:
                data.remove(p2)
                cl.append(p2)
    clusters.append(cl)
print([len(cl) for cl in clusters])
def acenter(cl):
    mas=[]
    for p1 in cl:
        sm=0
        for p2 in cl:
            sm+=dist(p1,p2)
        mas.append([sm,p1])
    return max(mas)[1]
centers=[acenter(cl) for cl in clusters]
print(centers)
px=centers[2][0]
py=centers[1][1]
print(int(px*10_000),int(py*10_000))