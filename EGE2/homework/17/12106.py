f=open('../../files/17_12106.txt')
mas=[int(i) for i in f]
mn=min([i for i in mas if ((i%117==0) and (i>0))])
k=0
mns=10**9
for i in range(len(mas)-1):
    if ((mas[i]<0) != (mas[i+1]<0)) and ((mas[i]+mas[i+1])%mn==0):
        k+=1
        mns=min(mns,mas[i]**2+mas[i+1]**2)
print(k,mns)