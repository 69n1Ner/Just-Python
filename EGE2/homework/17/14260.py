f=open('../../files/17_14260.txt')
mas=[int(i) for i in f]
mn=10**9
k=0
mx=0
for l in mas:
    if l>0 and len(str(l))==4 and (str(l)[-1]==str(l)[-2]):
        mn=min(mn,l)
for i in range(len(mas)-2):
    if len(str(abs(mas[i])))==3 and len(str(abs(mas[i+1])))==3 and len(str(abs(mas[i+2])))==3:
        if (mas[i]+mas[i+1]+mas[i+2] )>mn:
            k+=1
            mx=max(mx,mas[i]+mas[i+1]+mas[i+2])
print(k,mx)
#Забыл про модуль