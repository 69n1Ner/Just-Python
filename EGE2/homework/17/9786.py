f=open('../../files/17_9786.txt')
mas=[int(i) for i in f]
mx=-10**9
mxs=-10**9
for el in mas:
    if abs(el)%100==25:
        mx=max(mx,el)
k=0
for i in range(2,len(mas)):
    co=0
    for n in range(3):
        if 999<abs(mas[i-n])<10_000:
            co+=1
    if co>2:
        continue
    if mas[i-2]+mas[i-1]+mas[i]<=mx:
        k+=1
        mxs=max(mxs,mas[i-2]+mas[i-1]+mas[i])
print(k,mxs)