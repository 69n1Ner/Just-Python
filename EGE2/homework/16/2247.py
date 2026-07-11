from functools import lru_cache


@lru_cache(None)
def f(n):
    if n<3:
        return n+1
    if n>=3 and n%2==0:
        return f(n-2)+n-2
    if n>=3 and n%2!=0:
        return 0
k=0
for n in range(1,100000):

    if 9999<f(n)<100000:
        k+=1

print(k)