f=open('../../files/17_4415.txt')
mas=[int(i) for i in f]
k=0
mx=0
for x in range(len(mas)):
    for y in range(x,len(mas)):
        if (mas[x]-mas[y])%60==0:
            k+=1
            mx=max(mx,mas[x]-mas[y])
print(k,mx)