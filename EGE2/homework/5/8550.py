mn=10**9
for N in range(0,10000):
    n=bin(N)[2:]

    if N%3==0:
        n='10'+n[2:]+'21424'
    else:
        n= bin((N%3)*2)[2:] + n
    R=int(n,2)
    if R>8000:
        mn=min(R,mn)
print(mn)
