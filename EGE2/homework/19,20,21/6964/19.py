def f(s,h,l):
    if s>=100 and h==3:
        return 0
    if s>=100 and h<3:
        return 1
    if s<100 and h==3:
        return 1

    if h%2==0:
        return f(s+2,h+1,'A') or  f(s+4,h+1,'A') or f(s*2,h+1,'B')
    else: return f(s+2,h+1,'A') and  f(s+4,h+1,'A')
for s in range(1,100):
    if not f(s,1,''):
        print(s)