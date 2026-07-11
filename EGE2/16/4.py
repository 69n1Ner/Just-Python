from sys import *
setrecursionlimit(10**8)
k=0
h={}
def f(n):
    if n in h:
        return h[n]
    if n==0:
        h[n]= 0
        return 0
    elif n>0 and n%2==0:
        h[n]= f(n//2)
        return f(n//2)
    else:
        h[n] = 1+f(n-1)
        return 1+f(n-1)
for n in range(1,500+1):
    if f(n)==8:
        k+=1
print(k)