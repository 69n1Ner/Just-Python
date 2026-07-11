from itertools import permutations
print(*range(1,8))
s='26 147 456 237 37 13 245'.split()
v='BD DE EA AC CG GB GF FE FC'.split()

for i in permutations('ABCDEFG'):
    if all( str(i.index(b)+1) in s[i.index(a)] for a,b in v ):
        print(*i)