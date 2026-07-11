from functools import lru_cache


@lru_cache
def f(x, y, l,g):
    if x==18: g=1
    if x == 33: return 0
    if x>=y:return x==y and g==1
    if l=='C': return f(x + 1, y,  'A',g) + f(x + 3, y, 'B',g)
    return f(x + 1, y,  'A',g) + f(x + 3, y, 'B',g) + f(x * 2, y, 'C',g)

print(f(2, 51, '',0))
