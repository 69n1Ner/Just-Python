alp='0123456789AB'
for N in range(1,10000):
    s=''
    n=N
    while n:
        s=alp[n%12]+s
        n//=12
    if N%3==0:
        s='21424'+s+'B'
    else:
        s='2'+s+'0'
    R=int(s,12)
    if R<1996:
        print(R)