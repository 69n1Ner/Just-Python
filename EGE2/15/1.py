for A in range(600,0,-1):
    fl = True
    for x in range(0,600+1):
        f= x&51 == 0 or ((x&41 == 0) <= (x&A ==0))
        if not f:
            fl= False
            break
    if fl:
        print(A)