def f1(s,h,l):
    if s>=43 and h==3:
        return 1
    if s>=43 and h>3:
        return 0
    if s<43 and h==3:
        return 0
    if h%2==0:
        if l=='A':
            return f1(s + 2, h + 1, 'B') or f1(s*2,h+1,'C')
        if l=='B':
            return f1(s+1,h+1,'A') or f1(s*2,h+1,'C')
        if l=='C':
            return f1(s + 1, h + 1, 'A') or f1(s + 2, h + 1, 'B')
        return f1(s+1,h+1,'A') or f1(s+2,h+1,'B') or f1(s*2,h+1,'C')
    else:
        if l=='A':
            return f1(s + 2, h + 1, 'B') and f1(s*2,h+1,'C')
        if l=='B':
            return f1(s+1,h+1,'A') and f1(s*2,h+1,'C')
        if l=='C':
            return f1(s + 1, h + 1, 'A') and f1(s + 2, h + 1, 'B')
        return f1(s+1,h+1,'A') and f1(s+2,h+1,'B') and f1(s*2,h+1,'C')