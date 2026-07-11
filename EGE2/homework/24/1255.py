f=open('../../files/24_1255 (1).txt')
mx=0
for l in f:
    if l.count('A')>=25:
        continue
    #r=max(abs(l.index(x) - (len(l)-1-l[::-1].index(x))) for x in set(l))
    r = max(abs(l.index(x) - l.rfind(x)) for x in set(l))
    mx=max(mx,r)
print(mx)