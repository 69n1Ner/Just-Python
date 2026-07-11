for A in range(1000,0,-1):
    fl=True
    for x in range(0,900000000000):
        f=(((x%A==0)and(x%37==0))<=(x%3737==0))and(A<1000)
        if not f:
            fl=False
            break
    if fl:
        print(A)
        break