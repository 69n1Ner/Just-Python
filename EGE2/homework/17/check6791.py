f=open('../../files/17_6791.txt')
mas=[int(i) for i in f]
mn=10**9
for i in mas:
    if abs(i)%100==68:
        mn = min(mn,i)
mn=mn**2
k=0
mx=-10**9
for i in range(len(mas)-1):
    h=(abs(mas[i])%100)==68           #Внимательно с модулями
    h1=(abs(mas[i+1])%100)==68
    if (h!=h1) and (mas[i]**2+mas[i+1]**2)>=mn :
        k+=1
        mx=max(mx,mas[i]**2+mas[i+1]**2)
print(k,mx)

