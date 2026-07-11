for A in range(600,1,-1):
    fl=True
    for x in range(1,300):
        f=( not( (x%263==0)<=(x%A==0) ) )and(x%71==0)
        if f:
            fl=False
            break
    if fl:
        print(A)
        break