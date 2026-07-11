for A in range(0,600):
    fl=True
    for x in range(0,300):
        f= (x&49==0) <= ((x&28 !=0)<=(x&A!=0))
        if not f:
            fl= False
            break
    if fl:
        print(A)
        break