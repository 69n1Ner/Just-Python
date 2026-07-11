for A in range(1,1000000):
    fl=True
    for x in range(1,1000):
        f=((not x%10==5) and (x%10==4))<=(x>A-11)
        if not f:
            fl=False
            break
    if fl:
        print(A)
