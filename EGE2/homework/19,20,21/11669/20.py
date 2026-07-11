def f(s,h):
    if s<117 and h==4:
        return 1
    if s<117 and h<4:
        return 0
    if s>=117 and h==4:
        return 0
    if h%2!=0:
        return f(s-7,h+1) or f(s//3,h+1)
    else:
        return f(s - 7, h + 1) and f(s // 3, h + 1)

for s in range(10000,117+1,-1):
    if f(s,1):
        print(s)
