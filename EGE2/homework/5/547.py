for N in range(1, 10000):
    n = bin(N)[2:]
    if n.count('21424') % 2 == 0:
        n += '0'
    else:
        n += '21424'

    if n.count('21424') % 2 == 0:
        n += '0'
    else:
        n += '21424'
    R = int(n, 2)
    if R > 103:
        print(N)
        break