# f=[0]*11000
# for n in range(0,10100):
#     if n>10000:
#         f[n]=n+6
#     else:
#         f[n]=2*n+8+f[n+4]
# print(f[1092]-f[1104])
from functools import lru_cache

h={}
@lru_cache
def f(n):
    if n in h:
        return h[n]
    if n>10000:
        h[n]=n+6
        return n+6
    if n<=10000:
        h[n]=2*n+8+f(n+4)
        return 2*n+8+f(n+4)
for n in range(10001,1000,-1):
    f(n)
print(f(1092)-f(1104))