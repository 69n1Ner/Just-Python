from itertools import *
print(*range(1,8))
s='457 567 45 136 123 247 126'.split()
v='ab bg ge ef fa df da dc ce cb'.split()
for w in permutations('abcdefg'):
    if all(str(w.index(b)+1) in s[w.index(a)] for a,b in v):
        print(*w)