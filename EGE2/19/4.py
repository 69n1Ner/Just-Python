def f(s,s2,h):
    if s*s2>=123 and h==3:
        return 1

    elif s*s2<123 and h==3:
        return 0
    elif s*s2>=123 and h<3:
        return 0

    if h%2==0:
        return f(s+2,s2,h+1) or f(s,s2+2,h+1) or f(s*2,s2,h+1) or f(s,s2*2,h+1)
    else:
        return f(s + 2, s2, h + 1) or f(s, s2 + 2, h + 1) or f(s * 2, s2, h + 1) or f(s, s2 * 2, h + 1)
for s in range(1,40+1):
    if f(s,3,1):
        print(s)
