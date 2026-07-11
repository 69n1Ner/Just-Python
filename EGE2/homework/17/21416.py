f=open('../../files/17_21416.txt')
mas=[int(i) for i in f]
otr=0
for el in mas:
    if el<0:
        otr+=el
k=0
mx=-10**9
for i in range(2,len(mas)):
    if (max(mas[i-2],mas[i-1],mas[i])*min(mas[i-2],mas[i-1],mas[i]))>otr:
        k+=1
        mx=max(mx,mas[i-2]+mas[i-1]+mas[i])
print(k,abs(mx))