from collections import Counter
f=open('../../files/14251.txt')
for i,line in enumerate(f,start=1):
    l=line.split()
    smn=0
    smnc=0
    if sorted(Counter(l).values())==[1,1,1,2,2]:
        for el in l:
            if int(el)%2!=0:
                smnc+=int(el)
            if l.count(el)==2:
                smn+=int(el)
        if smn<=smnc:
            print(i,l)
            print(sum(map(int,l)))
            break
print(86*2+93*2,87+93+93+91)
