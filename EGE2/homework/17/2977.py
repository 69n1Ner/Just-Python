f=open('../../files/17_2977.txt')
mas=[int(i) for i in f]
mx=-1
k=0
for i in range(1,len(mas)):
    if (mas[i-1]**0.5)==int(mas[i-1]**0.5) and (mas[i-1]**0.5)%2==0 and (mas[i]**0.5)==int(mas[i]**0.5) and (mas[i]**0.5)%2==0:
        mx=max(mx,mas[i-1]+mas[i])
        k+=1
print(mx,k)