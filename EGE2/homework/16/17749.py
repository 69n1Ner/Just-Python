from functools import lru_cache


f=[0]*7004
for n in range(0,len(f)):
    if n>7000:
        f[n]=n+4
    else:
        f[n]=3*n+5+f[n+3]
#print(f[707]-f[716])
@lru_cache(None)
def f(n):
    if n>7000:
        return n+4
    else:
        return 3*n+5+f(n+3)
for n in range(7000,707+1,-1):
    f(n)
print(f(707)-f(716))