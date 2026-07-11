f=open('../../files/17_5292.txt')
mas=[int(i) for i in f]
mn=10**9
k=0
for m in mas:
    if m%123==0:
        mn=min(mn,m)
mx=0
for i in range(len(mas)-1):
    if (mas[i]%2023>=mn)!=(mas[i+1]%2023>=mn):
        k+=1
        mx=max(mx,mas[i]+mas[i+1])
print(k,mx)