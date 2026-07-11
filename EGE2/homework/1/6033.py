from itertools import *

s='234 156 17 15 246 257 36'.split()
v='GF FE ED DC CB BG GA BA AD'.split()
print(*range(1,8))
for l in permutations('ABCDEFG'):
    if all(str(l.index(b)+1) in s[l.index(a)] for a,b in v):
        print(*l)