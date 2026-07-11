def f(s1,s2,h):
    if s1+s2>=65 and h==3:
        return 1
    if s1+s2>=65 and h<3:
        return 0
    if s1+s2<65 and h==3:
        return 0
    if h%2==0:
        return f(s1+1,s2,h+1) or f(s1,s2+1,h+1) or f(s1*3,s2,h+1) or f(s1,s2*3,h+1)
    else:
        return f(s1+1,s2,h+1) or f(s1,s2+1,h+1) or f(s1*3,s2,h+1) or f(s1,s2*3,h+1)
for s in range(1,59):
    if f(s,6,1):
        print(s)