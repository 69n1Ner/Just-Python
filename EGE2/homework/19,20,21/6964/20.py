def f(s,h,l):
    if s>=98 and h==6:
        return 1
    if s<98 and h==6:
        return 0
    if s>=98 and h<6:
        return 0

    if h%2==0:
        return f(s+2,h+1,'A') or  f(s+4,h+1,'A') or f(s*2,h+1,'B')
    else: return f(s+2,h+1,'A') and  f(s+4,h+1,'A') and f(s*2,h+1,'B')
for s in range(1,100):
    if  f(s,1,''):
        print(s)