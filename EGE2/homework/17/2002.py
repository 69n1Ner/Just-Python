f=open('../../files/17_2002.txt')
mas=[int(i) for i in f]
mn=10**9
k=0
for i in range(3,len(mas)):
    d=0
    if mas[i-3]>mas[i-2]>mas[i-1]>mas[i]:

        d=mas[i-3]-mas[i]

        if d>1000:
            k+=1
            mn=min(mn,mas[i-3]+mas[i-2]+mas[i-1]+mas[i])

print(k,mn)