for E in range(-100,100):
    fl=True
    for x in range(-100,100):
        D = range(15,41)
        C = range(21,64)
        A = range(7,E+1)
        f=(x in D)<=(((not(x in C)) and (not(x in A)))<=(not(x in D)))
        if not f:
            fl=False
            break
    if fl:
        print(E)