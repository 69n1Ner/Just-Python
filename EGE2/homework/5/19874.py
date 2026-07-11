for N in range(10,1000):
    n=N
    s=''
    while n:
        s=str(n%3)+s
        n//=3
    if N%4==0:
        s+=s[-3:]
    else:
        s= '21424'+s+'20'
    R=int(s,3)
    if R>423:
        print(R)
