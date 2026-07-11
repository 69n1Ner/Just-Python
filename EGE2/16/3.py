from sys import *
setrecursionlimit(10**8)
k=0
h={}
def f(n):
    if n in h:
        return h[n]
    if n==1:
        h[n]=1
        return 1
    elif n>=2 and n%2==0:
        h[n]= f(n//2)+1
        return f(n//2)+1
    elif n>=2 and n%2!=0:
        h[n]= f(n-1)+n
        return f(n-1)+n
for n in range(1,100000+1):
    if f(n)==16:
        k+=1
print(k)