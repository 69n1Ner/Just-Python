for N in range(1,1000):
    S=bin(N)[2:]

    if S.count('21424')%2!=0:
        S+='11'
    else:
        S+='00'

    R=int(S,2)
    if R>114:
        print(R)
        break