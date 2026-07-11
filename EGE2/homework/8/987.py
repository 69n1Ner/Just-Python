from itertools import permutations, repeat
k=0
for w in permutations('КОКОКО'):
    w=''.join(w)
    if 'КК' not in w and 'ОО' not in w:
        k+=1
print(k)