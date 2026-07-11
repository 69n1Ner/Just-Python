f=open('../../files/17_2995.txt')
mas=[int(i) for i in f]
sr=sum(mas)/len(mas)
k=0
mx=0
for i in range(1,len(mas)):
    if mas[i-1]<sr and mas[i]<sr:
        if mas[i-1]%10==9 or mas[i]%10==9:
            k+=1
            mx=max(mx,mas[i-1]+mas[i])

print(k,mx)