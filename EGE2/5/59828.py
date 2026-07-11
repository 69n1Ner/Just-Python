for n in range(1,10000):
    s=n
    st=''
    while s:
        st=str(s%3)+st
        s//=3
    if n%3==0:
        st=st+st[-3:]
    else:
        s=(n%3)*3
        sn=''
        while s:
            sn = str(s % 3) + sn
            s //= 3
        st+=sn
    R=int(st,3)
    if R>150:
        print(n)
        break