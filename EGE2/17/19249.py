f=open('../files/17_19249.txt')
mas=[int(i) for i in f]
el=max([i for i in mas if (abs(i)%100==43 and 10000<=abs(i)<=99999)])
print(el)
el=el**2
k=0
mn=10**9
for h in range(len(mas)-2):
    if (10000<=abs(mas[h])<=99999 and abs(mas[h])%100==43) or \
            (10000<=abs(mas[h+1])<=99999 and abs(mas[h+1])%100==43) or \
            (10000<=abs(mas[h+2])<=99999 and abs(mas[h+2])%100==43):
        if (mas[h]**2 + mas[h+1]**2 + mas[h+2]**2)<=el:
            k+=1
            mn=min(mn,mas[h]**2 + mas[h+1]**2+mas[h+2]**2)
print(k,mn)
