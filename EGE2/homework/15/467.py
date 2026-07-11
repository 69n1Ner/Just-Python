k=0
for A in range(1,1000):
    fl=True
    for x in range(1,100):
        for y in range(1, 100):
            f=((x**2>60)or(not (x>A)))and((not (y**2>90))or(y>A))
            if not f:
                fl=False
                break
    if fl:
        k+=1
print(k)