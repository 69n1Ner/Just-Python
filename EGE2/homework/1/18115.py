from itertools import permutations
print(*range(1,8))
x='457 46 567 12 136 235 13'.split()
y='AB BD DF FE EC CA DG FG GC'.split()
for el in permutations('ABCDEFG'):
    if all(str(el.index(b) + 1) in x[el.index(a)] for a, b in y):
        print(*el)