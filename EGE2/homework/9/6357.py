f=open('../../files/6357.txt')
k=0
for s in f:
    stroka=s.split()
    fl=False
    sump=0
    sumn=0
    kp=0
    kn=0
    if len(stroka)==len(set(stroka)):
        continue
    for a in stroka:
        if stroka.count(a)==1:
            fl=True
            break
    if fl==False:
        continue
    for i in stroka:
        if stroka.count(i)==1:
            sumn+=int(i)
            kn+=1
        else:
            sump += int(i)
            kp += 1
    if sumn/kn<sump/kp:
        k+=1
print(k)