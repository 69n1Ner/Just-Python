from itertools import permutations

print(*range(1,9))
s='23 168 178 578 347 27 456 234'.split()
v='AF FC CG GH HE EA ED DB BG BH DF'.split()
for w in permutations('ABCDEFGH'):
    if all(str(w.index(b)+1) in s[w.index(a)] for a,b in v):
        print(*w)