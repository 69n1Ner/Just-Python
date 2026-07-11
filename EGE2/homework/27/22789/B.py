f=open('27_B_22789.txt')
f.readline()
clusters=[[],[],[]]
for l in f:
    x,y=map(float,l.split())
    if y>7:
        clusters[0].append([x,y])
    elif y<7 and x>0:
        clusters[1].append([x, y])
    else:
        clusters[2].append([x, y])
from math import dist

def f(cl):
    ms=[]
    for p1 in cl:
        po1=[]
        mas=[]
        for p2 in cl:
            mas.append([dist(p1,p2),p2])
        mas.sort()
        mas=mas[1:]
        for i in range(5):
            po1.append(mas[i][1])
        for i in range(10):
            po1.append(mas[len(mas)-i-1][1])
        sm=0
        for p in po1:
            sm+=dist(p1,p)
        ms.append([sm,p1])
    return min(ms)[1]
centers=[f(cl) for cl in clusters]
print(centers)
px=sum(x for x,y in centers)/len(centers)
py=sum(y for x,y in centers)/len(centers)

print(abs(int(px*10_000)),abs(int(py*10_000)))