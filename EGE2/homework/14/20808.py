mx=0
for x in range(2030,1,-1):
    s=7**170+7**100-x
    l=''
    co=0

    xm=0
    while s:
        l=str(s%7)+l
        s//=7
    co=l.count('0')
    if mx<=co:
        mx=max(mx,co)
        xm=x
        print(mx,xm)
print(xm)