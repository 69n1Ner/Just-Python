for N in range(1000,9999+1):
    S=str(N)
    a1=int(S[0])+int(S[1])
    a2=int(S[1])+int(S[2])
    a3=int(S[2])+int(S[3])

    amax=str(max(a1,a2,a3))
    asr= str(a1+a2+a3 - max(a1,a2,a3) - min(a1,a2,a3))

    R=asr + amax
    if R=='613':
        print(N)
        break