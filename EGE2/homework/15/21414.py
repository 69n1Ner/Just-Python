for A in range(0,1000):
    fl=True
    for x in range(0,1000):
        for y in range(0,1000):
            f=(5<y) or (x>32) or ((x+2*y)<A)
            if  not f:
                fl=False
                break
    if fl:
        print(A)
        break