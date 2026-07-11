def f(s,s2,h):
    if s+s2>=59 and h==2:
        return 1
    elif s+s2<59 and h==2:
        return 0
    elif s+s2>=59 and h<2:
        return 0

    if h%2!=0:
        return f(s+1,s2,h+1) or f(s,s2+1,h+1) or f(s*2,s2,h+1) or f(s,s2*2,h+1)
    else:
        return f(s + 1, s2, h + 1) or f(s, s2 + 1, h + 1) or f(s * 2, s2, h + 1) or f(s, s2 * 2, h + 1)
for s in range(2,53):
    if f(s,5,1):
        print(s)
        break