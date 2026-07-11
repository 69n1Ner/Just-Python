data=[]
f=open('27_A_18314.txt')
for l in f:
    x,y=list(map(float,l.replace(',','.').split()))
    data.append([x,y])

def manh_dist(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return abs(x2-x1)+abs(y2-y1)

clusters=[]
while data:
    cl=[data.pop()]
    for point in cl:
        for p1 in data:
            if manh_dist(point,p1) <3:
                cl.append(p1)
                data.remove(p1)
    clusters.append(cl)
print([len(cl) for cl in clusters])

def center(cl):
    mas=[]
    for point in cl:
        sm=0
        for p1 in cl:
            sm+=manh_dist(point,p1)
        mas.append([sm,point])
    return min(mas)[1]
centers=[center(cl) for cl in clusters]

px=sum(x for x,y in centers)/len(centers)
py=sum(y for x,y in centers)/len(centers)
print(int(px*1000),int(py*1000))