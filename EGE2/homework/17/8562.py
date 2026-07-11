f=open('../../files/17_8562.txt')
mas=[int(i) for i in f]
mn=10**9
for l in mas:
    if abs(l)<100 and abs(l)>9 and (abs(l)%10)==1:
        mn=min(mn,l)
k=0
mns=10**9
for i in range(len(mas)-1):
    x,y=mas[i],mas[i+1]
    if ( (x**2<mn**2) != (y**2<mn**2) ) and (x+y)>=0:
        k+=1
        mns=min(mns,mas[i]+mas[i+1])
print(k,mns)