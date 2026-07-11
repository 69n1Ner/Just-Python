from functools import lru_cache


@lru_cache
def f(n):
    if n<3:
        return 2
    if n >2:
        return 2*f(n-2)
for n in range(2223):
    f(n)
print(f(2222)/f(2182))