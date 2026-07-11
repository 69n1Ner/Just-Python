from functools import lru_cache


@lru_cache
def f(n):
    if n<=3:
        return 1
    if n>3:
        return (n+3)*f(n-2)
for n in range(2028):
    f(n)
print(f(2028)/f(2024))