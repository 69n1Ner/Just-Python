def f(s,h,l):
    if s>=43 and h==4:
        return 1
    if s>=43 and h<4:
        return 0
    if s<43 and h==4:
        return 0
    if h%2!=0:
        if l=='A':
            return f(s + 2, h + 1, 'B') or f(s*2,h+1,'C')
        if l=='B':
            return f(s+1,h+1,'A') or f(s*2,h+1,'C')
        if l=='C':
            return f(s + 1, h + 1, 'A') or f(s + 2, h + 1, 'B')
        return f(s+1,h+1,'A') or f(s+2,h+1,'B') or f(s*2,h+1,'C')
    else:
        if l=='A':
            return f(s + 2, h + 1, 'B') and f(s*2,h+1,'C')
        if l=='B':
            return f(s+1,h+1,'A') and f(s*2,h+1,'C')
        if l=='C':
            return f(s + 1, h + 1, 'A') and f(s + 2, h + 1, 'B')
        return f(s+1,h+1,'A') and f(s+2,h+1,'B') and f(s*2,h+1,'C')
for s in range(1,43):
    if f(s,1,''):
        print(s)