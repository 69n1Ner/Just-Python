def f(x,y):
    if x==y:
        return 1
    if x>y:
        return 0
    t=str(x)
    mx=max(map(int,t))
    return f(x+3,y) + f(x+mx,y)
print(f(10,24)*f(24,41))