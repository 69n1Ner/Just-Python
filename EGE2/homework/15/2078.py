for A in range(600,1,-1):
    fl=True
    for x in range(1,600):
        f=(( (x&13!=0)or(x&A!=0) )<=(x&13!=0) )or((x&A!=0)and(x&39==0))
        if not f:
            fl=False
            break
    if fl:
        print(A)
        break