def f(s,h):
    if s>=313 and h==3:
        return 1
    if s>=313 and h<3:
        return 0
    if s<313 and h==3:
        return 0
    if h%2==0:
        return f(s+2,h+1) or f(s+3,h+1) or f(s*3,h+1)
    else:
        return f(s+2,h+1) and f(s+3,h+1) and f(s*3,h+1)
for s in range(1,313):
    if f(s,1):
        print(s)