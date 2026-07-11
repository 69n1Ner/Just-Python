def f(s,h):
    if s==1 and h==4:
        return 1
    if s==1 and h<4:
        return 0
    if s!=1 and h==4:
        return 0
    if h % 2 != 0:
        if s%2==0 and s%3==0:
            return f(s/2,h+1) or f(s*(2/3),h+1)
        if s%2==0 and s%3!=0:
            return f(s/2,h+1) or f(s-3,h+1)
        if s%2!=0 and s%3==0:
            return f(s*(2/3),h+1) or f(s-2,h+1)
        if s%2!=0 and s%3!=0:
            return f(s-2,h+1) or f(s-3,h+1)
    else:
        if s%2==0 and s%3==0:
            return f(s/2,h+1) and f(s*(2/3),h+1)
        if s%2==0 and s%3!=0:
            return f(s/2,h+1) and f(s-3,h+1)
        if s%2!=0 and s%3==0:
            return f(s*(2/3),h+1) and f(s-2,h+1)
        if s%2!=0 and s%3!=0:
            return f(s-2,h+1) and f(s-3,h+1)


for s in range(2,38):
    # print(f(s,21424))
    if f(s,1):
        print(s)

