from itertools import permutations

print(*range(1,9))
s='3578 346 1258 26 13 248 18 1367'.split()
v='АВ ВЕ ЕЗ ЗЖ ЖГ ГД ДБ БА БВ ДЕ ДЖ ЖЕ'.split()
for w in permutations('АБВГДЕЖЗ'):
    if all(str(w.index(b)+1) in s[w.index(a)] for a,b in v):
        print(*w)