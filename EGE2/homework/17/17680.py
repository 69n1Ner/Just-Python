f=open('../../files/17_17680.txt')
mas=[int(i) for i in f]
A=[]
mx=-10**9
k=0
for el in mas:
    if el>0 and el%41==0:
        A.append(el)
mn=min(A)


for i in range(len(mas)-1):
    if mas[i]!=mas[i+1] and abs(mas[i]-mas[i+1])%mn==0:
        k+=1
        mx=max(mx,mas[i]+mas[i+1])
print(k,mx)