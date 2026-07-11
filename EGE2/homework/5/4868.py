for N in range(1,100000):
    n=str(N)
    s4=n.count('2')*2+n.count('4')*4+n.count('6')*6+n.count('8')*8
    s3=0
    if len(n)>2 and len(n)<4:
        s3=int(n[1])
    elif len(n)>3 and len(n)<6:
        s3 = int(n[1]) + int(n[3])

    R=abs(s3-s4)
    if R==13:
        print(N)
