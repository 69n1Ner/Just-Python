for A in range(0,600):
    fl=True
    for x in range(1,300):
        f= ((72%x==0)<=(90%x!=0)) or ((A-x)>80)
        if not f:
            fl= False
            break
    if fl:
        print(A)
        break