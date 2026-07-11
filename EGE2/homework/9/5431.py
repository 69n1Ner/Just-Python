f=open('../../files/5431.txt')
k=0
for l in f:
    line=l.split()
    mx=0
    fl=False
    for i in line:
        if line.count(i)==1:
            fl=True
            break
    if not fl:
        continue
    mx=max(map(int,line))
    line.remove(str(mx))
    mn=1
    for e in line:
        mn*=int(e)
    if mx**2>mn:
        k+=1
print(k)
