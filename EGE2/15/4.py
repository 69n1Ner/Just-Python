for A in range(0,600):
    fl=True
    for x in range(0,300):
        for y in range(0,300):
            f= (x*y<A) or (y>x) or (x>=8)
            if not f:
                fl= False
                break
    if fl:
        print(A)
        break