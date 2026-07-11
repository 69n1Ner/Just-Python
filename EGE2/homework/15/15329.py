for A in range(500,1,-1):
    fl=True
    for x in range(1,500):
        f=(not(x%A==0))<=( (x%28==0)<=(not(x%49==0)) )
        if not f:
            fl=False
            break
    if fl:
        print(A)
        break