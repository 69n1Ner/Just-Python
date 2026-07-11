cl1=[]
cl2=[]
cl3=[]
cl4=[]
cl5=[]
data=[]
f=open('27B_19747.txt')
def line(x,k,b):
    return k * x + b
for l in f:
    x,y=list(map(float,l.replace(',','.').split()))
    if line(x,1,0) < y and x<10:
        cl1.append([x,y])
    if line(x,1,0) > y and x<10:
        cl2.append([x,y])
    if x>10 and y<10:
        cl3.append([x, y])
    if line(x,1,0) < y and x>10:
        cl4.append([x,y])
    if 10<y<line(x,1,0) and x>10:
        cl5.append([x,y])

from math import dist
clusters=[cl1,cl2,cl3,cl4,cl5]
print([len(cl) for cl in clusters])
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