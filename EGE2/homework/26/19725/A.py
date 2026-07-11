f=open('26.7_19725.txt')
N=int(f.readline())
data=[int(l) for l in f]
data.sort()
sm=0
sm2=0
mas=[]
mas2=[]
from math import ceil
for el in data:
    if el<=250:
        sm+=el
        sm2+=el
    else:
        mas.append(el)
        mas2.append(el)
k=0
mas.sort(reverse=True)
for i in range(4,len(mas),4):
    sm+=ceil(mas[i-1]+mas[i-2]+mas[i-3]+mas[i-4]-min(mas[i-4],mas[i-1],mas[i-2],mas[i-3])+min(mas[i-4],mas[i-1],mas[i-2],mas[i-3])/3)
    k+=4
    mas[i - 1]=-1
    mas[i - 2]=-1
    mas[i - 3]=-1
    mas[i - 4]=-1
if len(mas)-k==4:
    sm+=ceil(mas[-1]+mas[-2]+mas[-3]+mas[-4]-min(mas[-4],mas[-1],mas[-2],mas[-3])+min(mas[-4],mas[-1],mas[-2],mas[-3])/3)
elif len(mas)-k==3:
    sm+=mas[-1]+mas[-2]+mas[-3]
elif len(mas)-k==2:
    sm+=mas[-1]+mas[-2]
elif len(mas)-k==1:
    sm+=mas[-1]
co=len(mas2)//4
mas2.sort()
mag=[0]*N
for i in range(3,len(mag),4):
    mag[i]=min(mas2)/3
    mas2.remove(min(mas2))
sm2+=sum(mag)+sum(mas2)
print(sm,ceil(sm2))
