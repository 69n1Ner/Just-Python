for N in range(1,128):
    n=f'{N:08b}'
    R=n.replace('21424','2')
    R=R.replace('0','21424')
    R=R.replace('2','0')
    R=int(R,2)+1
    if R==153:
        print(N)