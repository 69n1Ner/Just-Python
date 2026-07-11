for n in range(1000,9999+1):
    s=str(n)
    a1=int(s[0])+int(s[1])
    a2=int(s[1])+int(s[2])
    a3=int(s[2])+int(s[3])
    asr=str(a1+a2+a3 -max(a1,a2,a3)-min(a1,a2,a3))
    R=asr+str(max(a1,a2,a3))
    if R=='1315':
        print(n)