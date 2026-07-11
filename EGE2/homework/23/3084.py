def f(n,s):
    if n==s:
        return 1
    elif n>s:
        return 0
    sm=sum(map(int,str(n)))
    return f(n+2,s) + f(n+sm,s)
print(f(3,29)*f(29,68))

