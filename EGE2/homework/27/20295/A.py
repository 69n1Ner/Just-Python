f=open('27A_20295.txt')
data=[]
for l in f:
    x,y=list(map(float,l.split()))
    data.append([x,y])
from math import *
clusters=[]
while data:
    cl=[data.pop()]
    for point in cl:
        for p1 in data:
            if dist(point,p1)<0.4:
                cl.append(p1)
                data.remove(p1)
    clusters.append(cl)
print([len(cl) for cl in clusters])

def plotn(cl):
    mas=[]
    for point in cl:
        col=0
        for p1 in cl:
            if dist(point,p1)<=1:
                col+=1
        mas.append(col)
    return sum(mas)/len(mas)

plotn_s=[plotn(cl) for cl in clusters]
pmin=min(plotn_s)
pavg=sum(plotn_s)/len(plotn_s)
print(int(100000*pmin),int(100000*pavg))

