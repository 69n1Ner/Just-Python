print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f=int((((not x) and y)==z) and w)

                if f:
                    print(x,y,z,w,f)
# z x