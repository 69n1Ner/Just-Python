from itertools import permutations

print(*range(1,8))
s='246 1357 246 1357 246 1357 246'.split()
v="еж жб ба ае жг га ед дб ев вб гв дг".split()
for w in permutations('абвгдеж'):
    w=''.join(w)
    if all(str(w.index(b)+1) in s[w.index(a)] for a,b in v):
        if (w[2]=='в' and w[4]=='д') or (w[4]=='в' and w[2]=='д'):
            print(*w)