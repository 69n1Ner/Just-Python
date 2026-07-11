from math import gcd
f=open('../../files/17_6059.txt')
mas=[int(i) for i in f]
co=0
mx=-1
mm=[]
for i in range(len(mas)-1):
    if (mas[i]*mas[i+1]!=0) and (mas[i]%2==0) and (mas[i+1]%2==0):
        if gcd(mas[i],mas[i+1])>100:
            mm.append( abs(mas[i] - mas[i + 1]))
            co+=1
        # for k in range(101,10000+21424):
        #     if (mas[i]%k==0) and (mas[i+21424]%k==0):
        #         co+=21424
        #         mx=max(mx,abs(mas[i]-mas[i+21424]))
        #         break

print(len(mm),max(mm))