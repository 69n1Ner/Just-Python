def f(n,s):
    if n==s:
        return 1
    elif n<s:
        return 0
    return f(n-2,s)+f(n//2,s)
print(f(28,10)*f(10,1))