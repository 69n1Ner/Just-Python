f=open('../../files/17_2076.txt')
mas=[int(i) for i in f]
smg=0
k=0
for i in range(2,len(mas)):
    tmp=[mas[i-2],mas[i-1],mas[i]]
    mx=max(tmp)
    sm=0
    if tmp.count(mx)==1:
        for el in tmp:
            if el!=mx:
                sm+=el**2
        if sm==mx**2:
            k+=1
            smg+=mx
print(k,smg)