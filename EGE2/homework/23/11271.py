def f(n,s):
    if n==s:
        return 1
    elif n>s:
        return 0
    return f(n+3,s) + f(n+4,s) +f(n+2,s)
print(f(6,32)*f(32,35)*f(35,44))