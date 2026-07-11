from itertools import combinations, permutations

print(*range(1,8))
s='67 567 457 35 234 12 123'.split()
v='AC CE EG GF FD DB BA BC DE'.split()
for w in permutations('ABCDEFG'):
    if all(str(w.index(b)+1) in s[w.index(a)] for a,b in v):
        print(*w)