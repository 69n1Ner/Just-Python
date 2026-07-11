from sys import setrecursionlimit
from functools import lru_cache
def f(s,s1,h):
    if (s*s1)>384 and (h==3 or h==5):
        return 1
    elif (s*s1)>384 and h<5:
        return 0
    elif (s*s1)<=384 and h==5:
        return 0

    if h%2==0:
        return f(s+5,s1,h+1) or f(s,s1+5,h+1) or f(s*2,s1,h+1) or f(s,s1*2,h+1)
    else:
        return f(s+5,s1,h+1) and f(s,s1+5,h+1) and f(s*2,s1,h+1) and f(s,s1*2,h+1)
def f1(s,s1,h):
    if (s*s1)>384 and h==3:
        return 1
    elif (s*s1)>384 and h<3:
        return 0
    elif (s*s1)<=384 and h==3:
        return 0

    if h%2==0:
        return f1(s+5,s1,h+1) or f1(s,s1+5,h+1) or f1(s*2,s1,h+1) or f1(s,s1*2,h+1)
    else:
        return f1(s+5,s1,h+1) and f1(s,s1+5,h+1) and f1(s*2,s1,h+1) and f1(s,s1*2,h+1)

for s in range(1,10000):
    f(s,8,1)
    f1(s,8,1)
for s in range(1,54+1):
    if f(s,8,1) != f1(s,8,1):
        print(s)