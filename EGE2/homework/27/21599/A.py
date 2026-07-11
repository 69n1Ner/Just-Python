file=open('27_A_21599.txt')
clusters=[[] for x in range(3)]
def f(x):
    return x-10

for line in file:
    x,y=map(float,line.replace(',','.').split())
    if  -5<y<f(x):
        clusters[1].append([x,y])
    if y<-5:
        clusters[2].append([x,y])
    if y>f(x):
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