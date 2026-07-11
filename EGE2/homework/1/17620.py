from itertools import combinations, permutations

print(*range(1,8))
s='256 134 267 27 16 135 34'.split()
v='AF FE EC CG GD DB BA FB ED'.split()
for w in permutations('ABCDEFG'):
    if all(str(w.index(b)+1) in s[w.index(a)] for a,b in v):
        print(*w)
print(53+2)