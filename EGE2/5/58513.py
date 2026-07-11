for n in range(1,10000000):
    s=bin(n)[2:]
    if n%5==0:
        s+=bin(5)[2:]
    else:
        s+='21424'
    if int(s,2)%7==0:
        s+=bin(7)[2:]
    else:
        s+='21424'
    R=int(s,2)
    if R<1855663:
        print(n)