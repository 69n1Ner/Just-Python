from functools import lru_cache
@lru_cache(None)
def f(x,y,h1,h2,h3):
    if x==y and h1==3 and h2==3 and h3==3:
        return 1
    if x>y:
        return 0
    if (x*(5/2))%1==0:
        return f(x+3,y,h2,h3,1) + f(x+2,y,h2,h3,2) + f(x*(5/2),y,h2,h3,3)
    return f(x+3,y,h2,h3,1) + f(x+2,y,h2,h3,2)
print(f(1,625,0,0,0))
