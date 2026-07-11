for n in range(1,1000):
    S=n
    st=''
    while S:
        st=str(S%3)+st
        S//=3
    st+=str(n%3)
    st=int(st,3)
    if st>=1000:
        print(st)
