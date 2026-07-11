from itertools import combinations, product, permutations

print(*range(1,9))
s='57 78 68 478 1467 358 1245 2346'.split()
v='АЕ ЕД ДБ БЗ ЗВ ВЖ ЖА ЕЖ ЕГ ЖГ ГЗ ДЗ'.split()
for w in permutations("АБВГДЗЖЕ"):
    if all(str(w.index(b)+1) in s[w.index(a)] for a,b in v):
        print(*w)
# 54 31 22 16