from itertools import product, permutations
k=0
for w in permutations("ТЬЮРИНГ",6):
    w=''.join(w)
    if w[0]!='Ь' and 'ЮЬ' not in w and 'ИЬ' not in w:
        k+=1
        print(w)
print(k)