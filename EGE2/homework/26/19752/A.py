f=open('26_19752.txt')
f.readline()
mas=[]
g=open('temp.txt','w')
for l in f:
    m=list(map(int,l.split()))
    ida=m[0]
    k=m[1:]
    ln=len([y for y in k if y!=0])
    mas.append([ida,sum(k),sum([x for x in k if x>0]),ln])

mas.sort(key=lambda x: (-x[1],-x[2],-x[3],x[0]))
for el in mas:
    g.write(str(el[0])+' '+str(el[1])+' '+str(el[2])+' '+str(el[3])+'\n')

lns=len(mas)//3
last=mas[lns-1]
temp=mas[:lns]
print(lns)

for el in mas[lns:]:
    if el[1]==last[1] and el[2]==last[2] and el[3]==last[3]:
        temp.append(el)

i=len(temp)

other=mas[i:]
other=[x for x in other if x[1]>0]
per=int(len(other)*0.1)
last2=other[per-1]
itog=other[:per]
for el in other[per:]:
    if el[1]==last2[1] and el[2]==last2[2] and el[3]==last2[3]:
        itog.append(el)
# print(other[:per][-1],last2)
# print(len(other[:per]))
print(other[0][0],len(other))

#11840/4229/93992/3929(392)///(426,4229)///