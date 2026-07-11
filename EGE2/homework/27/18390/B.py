f=open('27_B_18390.txt')
R,K=map(float,f.readline().replace(',','.').split())
data=[]
for l in f:
    x,y=map(float,l.replace(',','.').split())
    data.append([x,y])
from math import dist
clusters=[]
while data:
    cl=[data.pop()]
    for p1 in cl:
        for p2 in data:
            if dist(p1,p2)<0.5:
                data.remove(p2)
                cl.append(p2)
    clusters.append(cl)

meds=[]
for cl in clusters:
    if len(cl)>400:
        meds.append(cl)
print([len(cl) for cl in meds])
print([len(cl) for cl in clusters])
def center(cl):
    mas=[]
    for p1 in cl:
        sm=0
        for p2 in cl:
            sm+=dist(p1,p2)
        mas.append([sm,p1])
    return min(mas)[1]
centers=[center(cl) for cl in meds]
print(len(centers))
def cs(clusters,cn):
    mas=[]
    for cl in clusters:
        for p1 in cl:
            sm=0
            for p2 in cn:
                sm+=dist(p1,p2)
            mas.append([sm,p1])
    return min(mas)[1]
centers1=cs(meds,centers)
print(int(centers1[0]*10_000),int(centers1[1]*10_000))