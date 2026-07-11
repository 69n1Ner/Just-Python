from itertools import combinations, permutations

print(*range(1,8))
s='24 135 256 157 234 37 46'.split()
v='ED DB BC CG GE AF DA FG FE'.split()
for w in permutations('ABCDEFG'):
    if all(str(w.index(b)+1) in s[w.index(a)] for a,b in v):
        print(*w)