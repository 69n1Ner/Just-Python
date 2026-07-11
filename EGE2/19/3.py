def f(s,h):
    if s>=172 and h==3:
        return 1
    elif s<172 and h==3:
        return 0
    elif s>=172 and h<3:
        return 0
    if h%2==0:
        return f(s+1,h+1) or f(s+2,h+1) or f(s+3,h+1) or f(s*2,h+1)
    else:
        return f(s+1,h+1) and f(s+2,h+1) and f(s+3,h+1) and f(s*2,h+1)
for s in range(1,171+1):
    if f(s,1):
        print(s)