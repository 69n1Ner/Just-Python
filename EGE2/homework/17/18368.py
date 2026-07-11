f=open('../../files/17_18368.txt')
mas=[int(i) for i in f]
mn=10**9
for el in mas:
    if abs(el)%10==7:
        mn=min(mn,el)
k=0
mx=-10**9
for i in range(2,len(mas)):
    if 9999<abs(mas[i-2])<100000 or 9999<abs(mas[i-1])<100000 or 9999<abs(mas[i])<100000:
        if (mas[i-2]*mas[i-1]*mas[i])%mn==0:
            k+=1
            mx=max(mx,mas[i-2]*mas[i-1]*mas[i])
print(k,mx)