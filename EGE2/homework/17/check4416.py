from itertools import permutations, repeat

f=open('../../files/17_4416.txt')
mas=[int(i) for i in f]

k=0
mx=0
for i in range(len(mas)):       #Двойной перебор
    for j in range(i+1,len(mas)):
        if (mas[i]+mas[j])%60==0 and (mas[i]%40==0 or mas[j]%40==0) and i!=j:
            k+=1
            mx=max(mx,mas[i]+mas[j])
print(k,mx)