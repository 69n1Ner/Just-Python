from itertools import product, repeat, combinations, permutations
k=0
for w in permutations('светлана'):
    w=''.join(w)
    if 'аа' not in w:
        k+=1
        print(w)
print(k//2)