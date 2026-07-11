from itertools import product, repeat
k=0
for s in product('0123456',repeat=6):
    fl=True
    if s[0]!='0' and s.count('6')==1:
        for c in range(len(s)-1):
            if (int(s[c])+int(s[c+1]))%2==0:
                fl=False
                break
        if fl:
            k+=1
print(k)