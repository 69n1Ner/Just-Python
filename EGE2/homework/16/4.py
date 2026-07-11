def f(n):
    if n<=3:
        return n
    elif n>3 and n<=32:
        return n//4+f(n-3)
    else:
        return 2*f(n-5)
print(f(100))