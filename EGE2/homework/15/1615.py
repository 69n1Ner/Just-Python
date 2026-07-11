for A in range(0,600):
    fl=True
    for x in range(0,600):
        for y in range(0,600):
            f=((11*x-y)!=53)or(x>y)or(A<x)
            if not f:
                fl=False
                break
    if fl:
        print(A)