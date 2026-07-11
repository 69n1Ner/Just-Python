from itertools import product, repeat, permutations
k=0
for w in permutations('ЯРЯРРЯР',5):
    w=''.join(w)
    if w.count("Я")<w.count('Р') and 'ЯЯ' not in w:
        k+=1
print(k)