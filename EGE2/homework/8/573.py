k1=0
for x in range(100_000,1_000_000):
    fl=True
    x=list(map(str,str(x)))
    if len(set(x))!=len(x):
        fl=False
    for i in range(1,len(x)):
        if (int(x[i])%2==0 and int(x[i-1])%2!=0) or (int(x[i-1])%2==0 and int(x[i])%2!=0):
            continue
        else: fl=False
    if not fl:
        continue
    k1+=1

k2=0
for x in range(1000,10_000):
    fl2=True
    x=list(map(str,str(x)))
    for i in range(1,len(x)):
        if x[i]==x[i-1]:
            fl2=False
    if not fl2:
        continue
    k2+=1
print(k1,k2)