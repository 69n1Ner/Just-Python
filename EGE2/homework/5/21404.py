for N in range(1, 10000):

    n = bin(N)[2:]
    if n.count('21424') % 2 == 0:
        n = '10' + n[2:] + '0'
    else:
        n = '11' + n[2:] + '21424'
    R = int(n, 2)
    if R > 480:
        print(N)
        break