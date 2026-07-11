f=open('../../files/17_6752.txt')
mas=[int(i) for i in f]
l=0
k=0
mx=-10**9
for n in mas:
    if n%3==0:
        l+=1
for i in range(len(mas)-1):
    if (mas[i]<0 or mas[i+1]<0) and (mas[i]+mas[i+1])<l:
        k+=1
        mx=max(mx,mas[i]+mas[i+1])
print(k,mx)