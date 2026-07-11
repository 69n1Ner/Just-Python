for A in range(43,56):
    fl=True
    for x in range(1000):
        f=((x&17!=0)<=((x&A!=0)<=(x&58!=0)))<=((x&8==0)and(x&A!=0)and(x&58==0))
        if f:
            fl=False
    if fl:
        print(A)