for A in range(1,300):
    fl=True
    for x in range(1,300):
        B=160<=x<=180
        f=B<=((x%35==0)<=(x%A==0))
        if not f:
            fl=False
            break
    if fl:
        print(A)
