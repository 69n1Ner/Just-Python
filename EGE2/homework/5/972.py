for N in range(100,999+1):
    n=str(N)
    k1=int(n[0])*int(n[1])
    k2=int(n[1])*int(n[2])
    R=str(max(k1,k2))+str(min(k1,k2))
    if int(R)==240:
        print(N)