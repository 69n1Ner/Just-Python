for A in range(1,600):
    fl=True
    for x in range(600):
        B=50<=x<=70
        f=(x%A==0)or((B)<=(not x%16==0))
        if not f:
            fl=False
            break
    if fl:
        print(A)