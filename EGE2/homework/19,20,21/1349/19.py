def f(s,h):
    if s==1 and h==3:
        return 1
    if s==1 and h<3:
        return 0
    if s!=1 and h==3:
        return 0
    if h%2==0:
        if (s%2==0 and s%3==0) or (s%2==0 or s%3==0):
            return f(s/2,h+1) or f(s*(1/3),h+1)
        if s%2:
            return f(s-2,h+1)
        if s%3:
            return f(s-3,h+1)
    else:
        if (s%2==0 and s%3==0) or (s%2==0 or s%3==0):
            return f(s/2,h+1) or f(s*(1/3),h+1)
        if s%2:
            return f(s-2,h+1)
        if s%3:
            return f(s-3,h+1)
for s in range(2,38):
    if f(s,1):
        print(s)
