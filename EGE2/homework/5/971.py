for N in range(9999,1000,-1):
    n=str(N)
    c12=int(n[0])*int(n[1])
    c34=int(n[2])*int(n[3])
    t=str(min(c12,c34))+str(max(c12,c34))
    R=int(t)
    if R==1214:
        print(N)
        break