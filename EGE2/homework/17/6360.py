f=open('../../files/17_6360.txt')
mas=[int(i) for i in f]
mn=10**9
for el in mas:
    if abs(el)%10==7:
        mn=min(mn,el)
k=0
mx=0
for i in range(len(mas)-1):
    if ((abs(mas[i])%10)==(abs(mas[i+1])%10)) and ((abs(mas[i])%7==0)!=(abs(mas[i+1])%7==0)):
        if (mas[i]**2+mas[i+1]**2)<=mn**2:
            k+=1
            mx=max(mx,mas[i]**2+mas[i+1]**2)
print(k,mx)