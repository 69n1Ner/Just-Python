from itertools import product, repeat
k=0
for w in product('ВИШНЯ',repeat=6):
    if w.count('В')<=1 and w[0]!='Ш' and w[-1]!="И" and w[-1]!="Я":
        print(w)
print(k)
