from sys import *
setrecursionlimit(10**8)

h={}
def f(n):
    if n in h:
        return h[n]
    if n==1:
        h[n]= 1
        return 1
    elif n>1:
        h[n]= 2*f(n-1)+n+3
        return 2*f(n-1)+n+3
print(f(19))