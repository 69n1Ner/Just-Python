f=open('../../files/8365.txt')
k=0
A=set()
for i in f:
    fl=True
    stroka=i.split()
    for j in stroka:
        if stroka.count(j)>=2:
            fl=False
            break
    if fl==False:
        continue
    for a in range(len(stroka)):
        for b in range(a,len(stroka)):
            if a!=b:
                for c in range(len(stroka)):
                    for d in range(c, len(stroka)):
                        if c!=a and c!=b and c!=d and b!=a and b!=d and d!=a:
                            sr1=(int(stroka[a])+int(stroka[b]))/2
                            sr2=(int(stroka[c])+int(stroka[d]))/2
                            ost=10-a-b-c-d
                            if sr1==int(stroka[ost]) and sr2==int(stroka[ost]):
                                temp=''.join(stroka)
                                A.add(temp)
                                print(stroka)
print(len(A))