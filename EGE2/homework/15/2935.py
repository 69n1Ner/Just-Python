for A in range(600,1,-1):
    fl=True
    for x in range(1,600):
        for y in range(1,600):
            f=((2*y+3*x)!=135)or(y>A)or(x>A)
            if not f:
                fl=False
                break
    if fl:
        print(A)
        break