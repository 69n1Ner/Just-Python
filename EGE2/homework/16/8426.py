def f(n):
    if n>1_000_000:
        return n
    if n<=1_000_000:
        return n+f(2*n)

def g(n):
    return f(n)//n
k=0
s=g(2000)
for n in range(1,10000):
    if g(n)==s:
        k+=1
print(k)
