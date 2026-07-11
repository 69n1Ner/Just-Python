from itertools import permutations, combinations

print(*range(1,8))
s='67 567 456 35 234 123 12'.split()
v='АБ БГ ГЕ ЕЗ ЗД ДВ ВА БВ ГД'.split()

for w in permutations('АБВГДЕЗ'):
    if all(str(w.index(b)+1) in s[w.index(a)] for a,b in v):
        print(*w)
