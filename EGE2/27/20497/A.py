f=open('27.19.A_20497.txt')
f1=open('1.txt','w')
data=[]
for l in f:
    x,y=list(map(float,l.split()))
    if (x<-1 and y>1) or (y>7) or (0.2<x<0.4 and -4<y<-2) or y<-6:
        pass
    else:
        data.append([x,y])
        # s=str(x)+' '+ str(y)+ '\n'
        # f1.write(s)
from math import dist
clusters=[]

while data:
    cl=[data.pop()]
    for point in cl:
        for p1 in data:
            if dist(point,p1) <1:
                cl.append(p1)
                data.remove(p1)
    clusters.append(cl)
print([len(cl) for cl in clusters])

def cr(cl):
    mas=[]
    mx=-10**9
    for point in cl:
        sm=0
        for p1 in cl:
            sm+=dist(point,p1)
        if sm >mx:
            mx=sm
            mas=point
    return mas

edges=[cr(cl) for cl in clusters]

tx=sum(x for x,y in edges)/len(edges)
ty=sum(y for x,y in edges)/len(edges)

print(int(tx*10000),int(ty*10000))
