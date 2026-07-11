from itertools import permutations

print(*range(1,8))
s='24 146 56 1267 36 23457 46'.split()
v='АБ БВ ВД ДЕ ЕК КГ ГВ ВЕ ГЕ АВ'.split()
for w in permutations('АБВГДЕК'):
    if all(str(w.index(b)+1) in s[w.index(a)] for a,b in v):
        print(*w)