f=open('../../files/17_2978.txt')
mas=[int(i) for i in f]
k=0
mn=10**9
for i in range(len(mas)-1):
    if (mas[i]+mas[i+1])**0.5==int((mas[i]+mas[i+1])**0.5) and ((mas[i]+mas[i+1])**0.5)%2==0:
        k+=1
        mn=min(mn,mas[i]+mas[i+1])
print(k,mn)