def f(s,s1,h):
    if s+s1>=131 and h==3:
        return 1
    elif s+s1>=131 and h<3:
        return 0
    elif s+s1<131 and h==3:
        return 0

    if h%2==0:
        return f(s+2,s1,h+1) or f(s,s1+2,h+1) or f(s*2,s1,h+1) or f(s,s1*2,h+1)
    else:
        return f(s+2,s1,h+1) or f(s,s1+2,h+1) or f(s*2,s1,h+1) or f(s,s1*2,h+1)
for s in range(1,122+1):
    if f(s,11,1)==1:
        print(s)