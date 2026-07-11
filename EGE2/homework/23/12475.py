from functools import lru_cache

ha=set()
@lru_cache(None)
def f(x,h):
    if h==68:
        ha.add(x)
        return 1
    if h>68:
        return 0
    f(x+1,h+1)
    f(x-2,h+1)

f(1,0)
print(len(ha))
