from itertools import product, repeat
k=0
for w in product('КАТЕР',repeat=3):
    if w.count('Р')>=2:
        k+=1
print(k)