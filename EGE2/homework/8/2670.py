from itertools import product, repeat
k=0
for w in product('СНЕГОВИК',repeat=5):
    if w[0]!='Е' and w[0]!='О' and w[0]!='И':
        if w[-1]!='Е' and w[-1]!='О' and w[-1]!='И':
            k+=1
print(k)