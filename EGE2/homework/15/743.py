
sm=0
for A in range(1,30000):
    fl=True
    for x in range(1,12,2):
        for y in range(3,13,3):
            f=(x<=(not y)) or A
            if not f:
                fl=False
                break
    if fl:
        sm+=A
print(sm)
