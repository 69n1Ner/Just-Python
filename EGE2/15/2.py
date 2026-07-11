for A in range(600,0,-1):
    fl=True
    for x in range(0,600):
        f= (not(x%A==0)) <= ((x%6==0) <= (not(x%9==0)))
        if not f:
            fl= False
            break
    if fl:
        print(A)