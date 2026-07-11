def f(s,s1,h):
    if (s+s1)<=100 and (h==5 and h==3):
        return 1
    elif (s+s1)<=100 and h<5:
        return 0
    elif (s+s1)>100 and h==5:
        return 0

    if h%2==0:
        return f(s-3,s1,h+1) or f(s,s1-3,h+1) or f(s//2,s1,h+1) or f(s,s1//2,h+1)
    else:
        return f(s-3,s1,h+1) and f(s,s1-3,h+1) and f(s//2,s1,h+1) and f(s,s1//2,h+1)
def f1(s,s1,h):
    if (s+s1)<=100 and (h==5 and h==3):
        return 1
    elif (s+s1)<=100 and h<5:
        return 0
    elif (s+s1)>100 and h==5:
        return 0

    if h%2==0:
        return f1(s-3,s1,h+1) or f1(s,s1-3,h+1) or f1(s//2,s1,h+1) or f1(s,s1//2,h+1)
    else:
        return f1(s-3,s1,h+1) and f1(s,s1-3,h+1) and f1(s//2,s1,h+1) and f1(s,s1//2,h+1)
for s in range(52,300):
    if f(s,48,1)!=f1(s,48,1):
        print(s)