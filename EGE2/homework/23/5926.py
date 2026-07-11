from functools import lru_cache

g=set()
def f(x,co,l):
    if co==24 :
        return {x}
    if l=='A':
        return f(x+7,co+1,'B') | f(x*4,co+1,'C')
    if l == 'B':
        return f(x + 1, co + 1, 'A') | f(x*4,co+1,'C')
    if l == 'C':
        return f(x + 1, co + 1, 'A') | f(x + 7, co + 1, 'B')
    return f(x+1,co+1,'A') | f(x+7,co+1,'B') | f(x*4,co+1,'C')

print(len(f(1,0,'')))