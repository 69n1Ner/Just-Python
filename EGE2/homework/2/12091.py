print('P Y H N F')
for P in range(2):
    for Y in range(2):
        for H in range(2):
            for N in range(2):
                F=Y and (not (Y or H)) or (not( Y<=H)) and (N<=P)
                if F:
                    print(P, Y, H, N, int(F))