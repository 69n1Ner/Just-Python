from itertools import product, repeat

alp='041'
mx=0
for s in product(alp,repeat=10):
    s=''.join(s)
    s+='<'
    while '4<' in s or '11<' in s or '00<' in s:
        if '11<' in s:
            s=s.replace('11<','<9',1)
        if '4<' in s:
            s=s.replace('4<','<5',1)
        if '00<' in s:
            s=s.replace('00<','<92',1)
    s=s.replace('<','')
    k=1
    for i in s:
        k*=int(i)
    if mx<=k:
        mx=k
print(mx)