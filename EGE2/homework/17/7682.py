f=open('../../files/17_7682.txt')
mas=[int(i) for i in f]
mx=-10**9
k4=0
k3=0
for el in mas:
    if el%570==0:
        mx=max(mx,abs(el))
for i in range(3,len(mas)):
    sr=(mas[i-3]+mas[i-2]+mas[i-1]+mas[i])/4
    if sr>mx:
        k4+=1
for i in range(2,len(mas)):
    co=0
    if mas[i-2]>0:
        co+=1
    if mas[i-1]>0:
        co+=1
    if mas[i]>0:
        co+=1
    if co>=2 and( mas[i-2]+mas[i-1]+mas[i])%34==0:
        k3+=1
print(k4,k3)