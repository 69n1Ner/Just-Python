def f(s,s1,h):
    if (s+s1)>=449 and h==4:
        return 1
    elif (s+s1)>=449 and h<4:
        return 0
    elif (s+s1)<449 and h==4:
        return 0

    if h%2!=0:
        return f(s+1,s1,h+1) or f(s,s1+1,h+1) or f(s*2,s1,h+1) or f(s,s1*2,h+1)
    else:
        return f(s + 1, s1, h + 1) and f(s, s1 + 1, h + 1) and f(s * 2, s1, h + 1) and f(s,s1*2,h+1)

for s in range(1,435+1):
    if f(s,11,1)==1:
        print(s)