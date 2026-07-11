for A in range(600,0,-1):
    fl=True
    for x in range(0,300):
        for y in range(0,300):
            f=not( (x<7) or (y>=(5*x+A-60)) or(x>=36) or (y<225) )
            if f:
                fl = False
                break
    if fl:
        print(A)
        break