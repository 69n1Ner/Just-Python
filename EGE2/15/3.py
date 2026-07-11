for A in range(600,0,-1):
    fl=True
    for x in range(0,300):
        for y in range(0,300):
            f= (x * y <100) or (y>= A) or (x>A)
            if not f:
                fl= False
                break
    if fl:
        print(A)