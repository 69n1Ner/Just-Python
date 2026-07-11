cl1=[]
cl2=[]
cl3=[]
f=open('27A_19747 (1).txt')
for l in f:
    x,y=list(map(float,l.replace(',','.').split()))
    if x<5:
        cl1.append([x,y])
    if y<5:
        cl2.append([x,y])
    if y>=5 and x>=5:
        cl3.append([x, y])
from math import dist
clusters=[cl1,cl2,cl3]
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
print(abs(int(px*100000)),abs(int(py*100000)))