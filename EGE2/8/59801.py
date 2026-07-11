from itertools import product
k=0
for w in product('КОНФЕТА',repeat=5):
    s=''.join(w)

    if s.count('Е')==2 and s[1]!='Ф':
        k+=1

print(k)