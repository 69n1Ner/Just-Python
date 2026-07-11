from collections import *
f=open('../../files/11830.txt')
co=0
for i in f:
    stroka=i.split()
    k=Counter(stroka)
    pp=1
    pn=1
    if len(k)==5 and sorted(k.values())==[1,1,1,2,2]:
        for j in k:
            if k[j]==2:
                pp*=int(j)**2
            else:
                pn*=int(j)
        if pp>2*pn:
            co+=1
print(co)