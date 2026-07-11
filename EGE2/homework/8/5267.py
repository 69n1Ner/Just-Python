from itertools import permutations
k=0
for w in permutations('LМФKБРАХИЙ'):
    w=''.join(w)
    if w[:2]=='LМ':
        print(w[:2])
        pass
    if w[-2:]=='KЙ':
        print(w[-2:])
        pass
    if w[:2]=='АМ' and w[-2:]=='ИЙ':
        k+=1

print(k)