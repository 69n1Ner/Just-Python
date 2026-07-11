def f(s1,s2,h):
    if (s1>=50 or s2>=50) and s1+s2<=109 and h==4:
        return 1
    if (s1>=50 or s2>=50) and s1+s2>109 and h==4:
        return 0
    if s1<50 and s2<50 and s1+s2<=109 and h==4:
        return 0
    if (s1>=50 or s2>=50) and s1+s2<=109 and h<4:
        return 0
    if h%2!=0:
        return f(s1+1,s2,h+1) or f(s1,s2+1,h+1) or \
            f(s1+1, s2, h + 1) or f(s1,s2+2,h+1) or \
            f(s1*2, s2, h + 1) or f(s1,s2*2,h+1)
    else:
        return f(s1 + 1, s2, h + 1) and f(s1, s2 + 1, h + 1) and \
            f(s1 + 1, s2, h + 1) and f(s1, s2 + 2, h + 1) and \
            f(s1 * 2, s2, h + 1) and f(s1, s2 * 2, h + 1)
# def f1(s1,s2,h):
#     if (s1>=50 or s2>=50) and s1+s2<=109 and h==2:
#         return 1
#     if (s1>=50 or s2>=50) and s1+s2>109 and h==2:
#         return 0
#     if s1<50 and s2<50 and s1+s2<=109 and h==2:
#         return 0
#     if (s1>=50 or s2>=50) and s1+s2<=109 and h<2:
#         return 0
#     if h%2!=0:
#         return f1(s1+1,s2,h+1) or f1(s1,s2+1,h+1) or \
#             f1(s1+1, s2, h + 1) or f1(s1,s2+2,h+1) or \
#             f1(s1*2, s2, h + 1) or f1(s1,s2*2,h+1)
#     else:
#         return f1(s1 + 1, s2, h + 1) and f1(s1, s2 + 1, h + 1) and \
#             f1(s1 + 1, s2, h + 1) and f1(s1, s2 + 2, h + 1) and \
#             f1(s1 * 2, s2, h + 1) and f1(s1, s2 * 2, h + 1)
for s in range(1,50):
    if f(s,24,1):
        print(s)
