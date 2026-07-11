def f(s,h):
    if s>=268 and h==4:
        return 1
    elif s>=268 and h<4:
        return 0
    elif s<268 and h==4:
        return 0

    if h%2!=0:
        return f(s+1,h+1) or f(s+3,h+1) or f(s*4,h+1)
    else:
        return f(s+1,h+1) and f(s+3,h+1) and f(s*4,h+1)

for s in range(1,267+1):
    if f(s,1)==1:
        print(s)