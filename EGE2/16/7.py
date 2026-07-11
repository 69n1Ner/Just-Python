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
        h[n]= 2*n*f(n-1)
        return 2*n*f(n-1)
print((f(2024)//16-f(2023))//f(2022))