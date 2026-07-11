for A in range(0,600):
    fl=True
    for x in range(1,1000):
        for y in range(1,1000):
            f=(x-3*y<A)or(y>400)or(x>56)
            if not f:
                fl=False
                break
    if fl:
        print(A)
        break