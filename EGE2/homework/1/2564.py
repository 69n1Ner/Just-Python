from itertools import product, combinations, permutations

print(*range(1,9))
s='58 34 28 268 17 478 568 13467'.split()
v='АЕ ЕЗ ЗЖ ЖБ БГ ГД ДВ ВА ЕД ЗД ДЖ'.split()
for i in permutations("АБВГДЕЖЗ"):
    if all( str(i.index(b)+1) in s[i.index(a)] for a,b in v ):
        print(*i)