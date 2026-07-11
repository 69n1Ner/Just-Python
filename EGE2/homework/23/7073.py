from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10**9)

@lru_cache
def f(x,y):
    if x==y:
        return 1
    if x>y:
        return 0
    if x==0:
        return f(x+3,y)
    if x==1:
        return f(x + 3, y)+f(x*2,y)
    if x<0:
        return f(x * x, y)+f(x+3,y)
    else:
        return f(x*x,y)+f(x*2,y)+f(x+3,y)
s=0

for x in range(-20,20+1):
    s+=f(x,20)
print(s)