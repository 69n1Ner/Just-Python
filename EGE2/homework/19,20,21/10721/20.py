t=[x for x in range(2,100,+2)]
def f(s,h):
    if s>=30 and h in t:
        return 0
    if s>=30 and h not in t:
        return 1
    if s<30 and h in t:
        return 1
    if h%3==0:
        return f(s+1,h+1) and f(s*2,h+1)
    if h%3==1:
        return f(s + 1, h + 1) and f(s * 2, h + 1)
    if h%3==2:
        return f(s + 1, h + 1) and f(s * 2, h + 1)
for s in range(1,30):
    if f(s,1):
        print(s)