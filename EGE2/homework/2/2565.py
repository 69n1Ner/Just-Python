print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f=( (w<=y) and ((not x) <= z)) <= ((z==w) or (y and (not x)) )
                if not f:
                    print(x,y,z,w, int(f))