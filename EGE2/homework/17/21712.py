f=open('../../files/17_21712.txt')
mas=[int(i) for i in f]
def ch(n):
    return 999<abs(n)<10_000 and abs(n)%10==6


mn=10**9
for el in mas:
    if el>0 and ch(el):
        if el%10==6:
            mn=min(mn,el)


k=0
mx=0
for el1,el2,el3 in zip(mas,mas[1:],mas[2:]):
    if (ch(el1)+ch(el2)+ch(el3))==1:
        if (el1+el2+el3)<=mn:
            k+=1
            mx=max(mx,el1+el2+el3)
print(k,mx)