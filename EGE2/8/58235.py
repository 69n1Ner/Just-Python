from itertools import product
k=0
for w in product('0123',repeat=3):
    s=''.join(w)

    if s[0]!='0' and s[2]+s[0]>s[1]+s[2]:
        print(s)
        k+=1

print(k)