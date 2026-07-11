f=open('../../files/2104.txt')
from math import dist
k=0
for l in f:
    x0,y0,x1,y1=list(map(int,l.strip().split()))
    p1=[x0,y0]
    p2=[x1,y1]
    if dist(p1,p2)  <=5 and ((p1[0]<0 and p2[0]>0) or (p1[1]<0 and p2[1]>0)):
        k+=1
print(k)