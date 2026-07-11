def f(s,s2,h):
    if s+s2>=464 and h==4:
        return 1
    elif s+s2<464 and h==4:
        return 0
    elif s+s2>=464 and h<4:
        return 0

    if h%2!=0:
        return f(s+2,s2,h+1) or f(s,s2+2,h+1) or f(s*3,s2,h+1) or f(s,s2*3,h+1)
    else:
        return f(s+2,s2,h+1) and f(s,s2+2,h+1) and f(s*3,s2,h+1) and f(s,s2*3,h+1)

for s in range(1,450+1):
    if f(s,13,1)==1:
        print(s)
